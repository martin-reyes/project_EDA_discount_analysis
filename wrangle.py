import pandas as pd
import os.path
import re

def acquire_store_data():

    filename = 'data/store_data_raw'
    
    # if file doesn't exist, acquire and cache
    if not os.path.isfile(filename):
    
        db = 'superstore_db'
        
        categories_query = "SELECT * FROM categories;"
        customers_query  = "SELECT * FROM customers;"
        orders_query     = "SELECT * FROM orders;"
        products_query   = "SELECT * FROM products;"
        regions_query    = "SELECT * FROM regions;"

        
        categories = pd.read_sql(categories_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        customers  = pd.read_sql(customers_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        orders     = pd.read_sql(orders_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        products   = pd.read_sql(products_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        regions    = pd.read_sql(regions_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        
        # join tables
        df = orders.merge(customers, on='Customer ID', how='left')
        df = df.merge(categories, on='Category ID', how='left')
        df = df.merge(regions, on='Region ID', how='left')
        df = df.merge(products, on='Product ID', how='left')

        df.to_csv(filename, index=False)
        
        return df
    
    return pd.read_csv(filename)


def prep_store_data(df = acquire_store_data()):
    """
    Preprocesses and cleans the store data DataFrame.
    
    Args:
    df (DataFrame): Input DataFrame containing raw store data.
    
    Returns:
    DataFrame: Prepared DataFrame with cleaned columns and new features.
    """
    # Clean column names by converting to lowercase and replacing white spaces with underscores
    df.columns = [re.sub(r'[^a-zA-Z]', '_', col.lower()) for col in df.columns]

    # Drop foreign key columns
    df = df.drop(columns=['customer_id', 'product_id', 'category_id', 'region_id'])
    
    # Convert date columns to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])
    
    # Convert postal_code and quantity columns to integers
    df['postal_code'] = df['postal_code'].astype(int)
    df['quantity'] = df['quantity'].astype(int)
    
    # Extract order month and year from order_date
    df['order_month'] = df['order_date'].dt.month
    df['order_year'] = df['order_date'].dt.year
    
    # Calculate cost column
    df['cost'] = df['sales'] - df['profit']
    
    return df