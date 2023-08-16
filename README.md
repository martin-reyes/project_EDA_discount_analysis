<a name="top"></a>

# Store Discount Analysis

by Martin Reyes

## Project Description

In this EDA project, superstore transaction data is acquired from a SQL database and prepared in Python. This data can then be analyzed to see if discount rates drive sales while maintaining profits for the company. Analysis will also be done to see how discount rates drive customer retention.

Through this analysis, actionable recommendations will be provided to enhance the company's overall sales performance and strategic decision-making.

 
## Project Goals

**EDA Goals and Questions:**

**1. Univariate Analysis** for summary of transactions and items sold

**2. Optimal Discount Rates:** Determine the optimal discount rates for business metrics.

&nbsp;&nbsp;&nbsp;**Bivariate Analysis:** Discount vs. Profit/Sales/Margin
<br>&nbsp;&nbsp;&nbsp;Group by discount and analyze sales, profit, margin, and quantity

- How do different discount rates impact sales?
- Do higher discounts lead to a significant decrease in profitability due to increased costs or reduced margins?
- Do customers tend to buy more items when discounts are applied?
- Is there a specific discount percentage that leads to the highest profit margins?

&nbsp;&nbsp;&nbsp;**Multivariate Analysis:** Discount vs. Profit/Sales/Margin on low, medium, and high-priced items
<br>&nbsp;&nbsp;&nbsp;Group items into certain price ranges and analyze the questions above again

- Stats test to compare business metrics between discounted and non-discounted items.

**4. Customer Impact:** Analyze customer response to discounts.

&nbsp;&nbsp;&nbsp;Do returning customers see more discounted orders than non-returning customers?

&nbsp;&nbsp;&nbsp;Are discounts and customer return dependent of each other?
- perform $\chi^2$ test to see if there is a dependent relationship between customer return and discounts.


## Initial Thoughts

The following initial hypotheses will lead the analysis:

1. **Small discounts increased sales**: It's likely that smaller discounts will lead to more sales. Customers are more inclined to make purchases when they perceive a deal, even if the discount is relatively small. Small discounts will slightly decrease margins, but the increase in sales will lead to profit gain.

2. **Optimal Discount Threshold**: There may be a discount threshold, around 20-30%, where the impact on sales plateaus while profits start to decline significantly. This would indicate that customers might not respond as positively to deeper discounts, and the cost of those discounts outweighs the additional sales generated.

3. **Profit-Maximizing Discount Rate**: There may exist an optimal discount rate that produces the best profit margin. This would be a balance between attracting customers with appealing discounts and maintaining healthy margins that contribute to overall profitability.

4. **Customer Retention through Discounts**: Discounts will lead to customer retention. If customers feel they are getting value from the discounts, they might be more likely to return for future purchases. Analyzing the relationship between discounts and customer retention can offer insights into the long-term impact of certain discount strategies.

 
## The Plan
 
* **Acquire** store data
1. Read tables from MySQL
2. Join tables in Python
 
* **Prepare** data 
1. Rename [columns](#data-dictionary)
1. Check for missing values
    1. Check for empty string values
1. Drop duplicate columns (foreign keys)
1. Check for duplicate rows
1. Ensure correct data types
1. Univariate analysis
    1. View value counts
    1. Note outliers and handle appropriately
    1. View distributions of numeric data
1. Engineer features that may be useful

* **Explore** data to answer EDA goals and questions


---

## Analytical Findings

During exploration of the sales data, several noteworthy insights were uncovered to shed light on the effectiveness of different discount rates and their impact on profits, sales, and quantity of items sold.

### Optimal Discount Rates and Profit Generation

- 10% discount rates generate the most profit. However, few items are sold at this discount rate and those that are are expensive items. Thus, there is not enough evidence to conclude that this is the optimal discount rate that would drive sales while maintaining profit.
- A sufficient amount of data is only available for the 20% discount rate, making it challenging to compare its performance against other discount rates. <u>**Further data collection would be required to draw meaningful conclusions**</u> in this regard.

### Mann-Whitney's Test Conclusions: Do Discounts Drive Business Metrics as Expected?

Short Answer: **No**

- **Sales:** With the exception of cheap items, discounted items lead to decreased sales. Discounted cheap items show no significant difference in sales compared to non-discounted cheap items.
- **Profit:** Discounted items significantly reduce profits.
- **Quantity:** Discounted items do not seem to have a significant impact on the quantity of items sold.

### Chi-Square Test Conclusion: Do Discounts Drive Customer Return?

Short Answer: **No**

- The chi-squared test results indicate that <u>**the data is not significant enough to conclude that offering a discount leads to an increase in customer retention**</u>. The observed proportions of discounted orders from returning and non-returning customers are similar to the expected proportions that would seen if discounts and customer return were independent.

### Correlations between Profit and Item Price

- Another interesting finding is that both profit and profit margin exhibit a negative correlation with cost and price. This indicates that <u>**higher-priced items are not yielding as much profit as lower-priced items**</u>.


## Summary

In summary, our initial thoughts on discount effects, which were ideal effects for the business, did not turn out to be true. Discounts are not increasing sales or maintaining profits. Discounts are also not driving customer return or quantity of items sold. There was not enough data to find an optimal discount rate that would drive sales and maintain profit.

## Recommendations and Next Steps

Based on the insights gained from the exploration of the sales data, the following recommendations and next steps can be suggested to guide the company's approach towards discounts:

**Data Collection for Optimal Discount Rates:** Since the exploration did not yield sufficient data to conclusively identify the optimal discount rate that maximizes both sales and profits, more data should be gathered across a wider range of discount rates. This will allow for a more comprehensive analysis and evidence-based decision-making.

**Impact on Customer Loyalty:** Delve deeper into customer behavior after a discount. Implement post-purchase surveys or feedback mechanisms to understand whether discounts influence customer loyalty, repeat purchases, and overall satisfaction.

**Promotional Strategies:** On the same note, consider promoting or emphasizing discounts to attract customers and drive customer loyalty.

**Continuous Monitoring and Analysis:** Sales dynamics and customer preferences can evolve over time. Sales data should be analyzed regularly to identify emerging trends, revisit discount strategies, and adjust discounts as needed.

In conclusion, the exploration of the sales data has highlighted the relationships between discounts, profits, and customer behavior. Implementing the above recommendations and next steps will allow the company to make more informed decisions about discount strategies, better cater to customer needs, and optimize overall profitability.

[Back to top](#top)

---


<a name="data-dictionary"></a>
## Data Dictionary

| Feature    | Definition             | Feature      | Definition          |
|:-----------|:-----------------------|:-------------|:--------------------|
| order_id   | Order ID               | order_date   | Date when the order was placed|
| ship_date  | Date when the order was shipped | customer_id | Customer ID   |
| ship_mode  | Shipping method for the order   | segment     | Customer segment  |
| city       | City where the order was placed |  product_id | Product ID       |
| postal_code | Postal code of the order's destination | category | Product category |
| sales  | Total sales value of the order  | quantity | Quantity of products ordered |
| discount | Discount applied to the order | profit | Profit generated from the order|
| category_id | Category ID for the product | region_id | Region ID of the order's destination  |
| customer_name | Customer name    | state  | State where the order was placed  |
| sub_category | Product sub-category | region_name   | Region of the order's destination |
| product_name | Product name                           | | |


[Back to top](#top)