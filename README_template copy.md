<a name="top"></a>

# `Project_Title`

by `NAME`

<!-- <p>
  <a href="https://github.com/martin-reyes" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3291/3291695.png" alt="GitHub" width="40" height="40">
  </a>

  <a href="https://www.linkedin.com/in/martin-reyes-ds/" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" alt="LinkedIn" width="40" height="40">
    </a>
</p>
 -->

## Project Description

`Description: Background, Goals, Outcomes/Insights`

 
## Project Goals

```
* Goal 1 (e.g. explore goal(s))
* Goal 2 (e.g. model goal(s))
* etc.
```

 
## Initial Thoughts
 
`Initial thought(s)/hypotheses`
 
## The Plan
 
* **Acquire**
 
* **Prepare** data. 
    1. Inspect raw data and note any desired transformations which may include any of the following:
        * Drop unnecessary columns (duplicate, redundant columns)
        * Numeric columns should be numeric data types
        * Handle missing values and impute appropriate values
            * check for explicit missing values (e.g. `np.nan`)
            * check for implicit missing values (e.g. whitespace, `'unknown'`, etc.)
        * Deal with any duplicate rows
        * Address and encode categorical columns
            * one-hot encode unordered categorical columns
            * label encode ordered categorical columns  
    1. Inspect clean data
        * Ensure data is tidy:
            * one value per cell
            * each observation is one and only one row
            * each feature is one and only one column
    1. Split the data
        * Determine if target column has class imbalance. If, so stratify.
        * Perform `70/15/15 train/validate/test` split.
        * **`set RANDOM_STATE`**
    1. Create data dictionary
    1. Summarize data transformations

* **Explore** data in search of `target` drivers
   1. General Inspect
       - `.info()` and `.describe()`
       - identify continuous and categorical columns
   1. Univariate Stats: 
       - Categorical
       - Nunerical
   1. Bivariate Stats:
       - Categorical features to target relationships
       - Continuous features to target relationship
       
   Ask Specific questions:
   - e.g. How does `col1` relate to `target`?
      
* Develop a **model** to predict `target`
   * Use drivers identified in explore to build predictive models
   * Create and run a baseline model with `sklearn`'s `DummyClassifier` to compare our results to
   * Create and run `KNN`, `Logistic Regression`, and `Decistion Tree` classification models
   * Use the insights from the highest-performing model (with highest test `accuracy`) to confirm our initial hypotheses and insights on the features that are the biggest drivers of churn
   
* **Evaluate** models on train and validate data
   * Identify the metric to maximize
       * Do we simply want an accurate model?
       * If not, is it more costly to incorrectly identify non-churning customers (FN) or churning customers (FP)?
   * Select the best model based on highest desired metric

* Evaluate the best model on validation data set. After we find the best model, test on the test set.
    * Save test predictions to a file (e.g. csv file)
 
* Draw conclusions
 
 
<a name="data-dictionary"></a>
## Data Dictionary

| Feature              | Definition |
|:----------------------|:-------------------- |

 
## Steps to Reproduce

 
## Takeaways and Conclusions

Key drivers of `target`:

Best performing ML model:

 
## Recommendations


## Next Steps
With more time, we can:
- Do multivariate analysis and see how a combination or columns relate to churn 
- Develop a better-performing model by feature engineering, feature scaling, running other ML classifiers, etc.
- If we want to take action with any of the recommendations, we can change our performance metric to precision or recall, and predict and target customers this way.
- Gather more data and features


[Back to top](#top)