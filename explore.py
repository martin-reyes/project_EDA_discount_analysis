import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import patches
import numpy as np
import pandas as pd

from scipy import stats


def plot_counts(df, columns):
    for col in columns:
        if df[col].nunique() < 20 or\
            (not pd.api.types.is_numeric_dtype(df[col]) and df[col].nunique() < 10):
            print(col.upper())
            # Calculate raw counts and normalized counts
            counts = df[col].value_counts()
            frequencies = counts / counts.sum()

            # Create a figure with two subplots
            fig, axes = plt.subplots(1, 2, figsize=(10, 4))

            # Plot raw countplot in the first subplot
            sns.barplot(x=counts.index, y=counts.values,
                        color='#2F8A70', ax=axes[0])
            axes[0].set_title('Counts')

            # Plot normalized countplot in the second subplot
            sns.barplot(x=frequencies.index, y=frequencies.values,
                        color='#2F8A70', ax=axes[1])
            axes[1].set_title('Frequencies')

            # Add annotations to the bars in the normalized countplot
            for i, ax in enumerate(axes):
                for p in ax.patches:
                    annotation = f'{p.get_height():.0f}' if i == 0\
                                                     else f'{p.get_height() * 100:.0f}%'
                    ax.annotate(annotation, (p.get_x() + p.get_width() / 2, p.get_height()),
                                ha='center', va='bottom')

            
            # Adjust layout and display the plots
            plt.tight_layout()
            sns.despine()
            plt.show()
            
def plot_correlations(df):
    corr_df = df.select_dtypes(include=['number']).iloc[:, [1, 2, 3,
                                                        4, 7, 8, 9]]

    plt.figure(figsize=(len(corr_df.columns),
                        len(corr_df.columns) * .6))

    mask = np.triu(np.ones_like(corr_df.corr().iloc[1:,:-1]),k=1)
    sns.heatmap(corr_df.corr().iloc[1:,:-1], mask=mask, linewidths=.5, annot=True,
                         cmap='RdYlGn', vmin=-1, vmax=1, square=True)
    
    ax = plt.gca()
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(right=False, labelsize=8) 
    cbar.set_ticks([-1, -.5, 0, .5, 1])
    
    plt.tick_params(axis='both', left=False, bottom=False)

    highlighted_cells = [(3, 3), (3, 5), (4, 4), (5, 5)]

    for cell in highlighted_cells:
        rectangle = patches.Rectangle((cell[0], cell[1]), 1, 1, linewidth=2,
                                      edgecolor='black', facecolor='none')
        ax.add_patch(rectangle)
    
    plt.xticks(rotation=15)
    plt.show()
    
def analyze_discount_rates(df):
    print('Counts:')
    display(pd.DataFrame([
                df.groupby('discount_bin').size(),
                round(df.groupby('discount_bin').size() / len(df), 2)
            ]).T.rename(columns={0: 'counts', 1: 'frequencies'}))
    
    aggregation_functions = {
    'sales': ['median', 'sum'], 'profit': ['median', 'sum'],
    'margin': ['median'], 'quantity': ['median', 'sum']}

    print('Metrics:')
    display(df.groupby('discount_bin')[['sales', 'profit', 'cost',
                                        'margin', 'quantity']]\
                                      .agg(aggregation_functions).round(2))
    
    
def plot_metric_distributions(df, item_type_string):
    
    low_disc_df = df[df['discount_bin'] == '0 - .2']
    non_disc_df = df[df['discount_bin'] == '0']
    
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(8,7.5))

    metrics = ['sales', 'profit', 'quantity']
    data = [low_disc_df, non_disc_df]
    colors = ['blue', 'orange']
    disc_strs = ['Low-', 'Non-']
    
    for row in range(3):
        for col in range(2):
            sns.histplot(data=data[col], x=metrics[row],
                         bins=20, color=colors[col], ax=axes[row, col])
            axes[row, col].set_title(f'{metrics[row].capitalize()} for {disc_strs[col]}Discounted,\n{item_type_string} Items')

    # Adjust layout and display the plots
    plt.tight_layout()
    sns.despine()
    plt.show()
    
def run_mann_whitneys_test(df, metric):
    
    # set hypothesis
    H0 = f"Null Hypothesis: Average {metric} for low-discounted items and non-discounted items are equal."
    Ha = f"Alternative Hypothesis: Average {metric} for low-discounted items and non-discounted items are not equal."
    
    low_disc_df = df[df['discount_bin'] == '0 - .2']
    non_disc_df = df[df['discount_bin'] == '0']
    
    # calculate test statistics and p-value.
    u_stat, p_val = stats.mannwhitneyu(low_disc_df[metric], non_disc_df[metric])
    
    return H0, Ha, u_stat, p_val


def run_mann_whitneys_tests(cheap_df, med_df, exp_df, v_exp_df):
    # List to store results
    results = []

    # Iterate over data frames and metrics
    for i, data in enumerate([cheap_df, med_df, exp_df, v_exp_df]):
        names = ['\$0 - \$20', '\$20 - \$100', '\$100 - \$300', '$300+']
        for metric in ['sales', 'profit', 'quantity']:
            H0, Ha, u_stat, p_val = run_mann_whitneys_test(data, metric)
            result = 'yes' if p_val < .05 else 'no'
            results.append({'item_price': names[i], 'metric': metric,
                            'H0': H0, 'Ha': Ha, 'u_Statistic': u_stat,
                            'p-value': p_val, 'significant_difference': result})

    # Create a DataFrame from the results list
    return pd.DataFrame(results).round(3).sort_values('metric')  

def items_to_orders(df):
    # Grouping by order_id to make orders DataFrame 
    orders = df.groupby('order_id').agg({
        'order_date': 'first',  'ship_date': 'first',       'ship_mode': 'first',
        'city': 'first',        'state': 'first',           'postal_code': 'first',
        'sales': 'sum',         'quantity': 'sum',          'discount': 'sum',
        'profit': 'sum',        'customer_name': 'first',   'order_month': 'first',
        'order_year': 'first',  'cost': 'sum',    'margin': 'sum',   'price': 'sum',
    })

    # Adding a column for returning customers
    customer_order_counts = df['customer_name'].value_counts()
    orders['returning_customer'] = orders['customer_name'].apply(lambda x: 1\
                                                                           if customer_order_counts[x] > 1
                                                                           else 0)

    # Adding a column for orders with discounts
    orders['has_discount'] = orders['discount'].apply(lambda x: 1 if x > 0 else 0)

    # Resetting the index
    orders.reset_index(inplace=True)

    return orders


