Include your answers to this afternoon's exercies in `afternoon.py`.

This afternoon you will be introduced to the basics of linear regression.

## Part 0: Solving the Normal Equation

The beta coefficients of a linear regression model can be calculated by
solving the normal equation. 


1. Load the data in by the following code:

   ```python 
   import statsmodels.api as sm
   prestige = sm.datasets.get_rdataset("Duncan", "car", cache=True).data
   y = prestige['prestige']
   x = prestige[['income', 'education']].astype(float)
   ```
   
   **Hint:**
   - **The features (x) should be scaled (centered by mean and divided by standard deviation)**
   - **After scaling, append a column of 1's to the feature matrix (x),
     so an intercept can be fitted.**


2. Using numpy, write a function that solves the **normal equation** (below).
   As input your function should take a matrix of features (**x**) and
   a vector of target (**y**). You should return a vector of beta coefficients 
   that represent the line of best fit which minimizes the residual. 
   Calculate  R<sup>2</sup>. 
   
   <div align="center">
      <img height="30" src="images/normal_equation.png">
   </div>

3. Verify your results using statsmodels. Use the code below as a reference.
   ```python
   import statsmodels.api as sms
   model = sms.OLS(y, x).fit()
   summary = model.summary()
   ```

## Part 1: Linear Regression Diagnosis

The linear regression model makes a number of assumptions about the data, including 

- **Homoscedasticity of residuals**
- **Normal distribution of residual**
- **Lack of mutlicollinearity between features**
- **Lack of autocorrelation (if the data is a time series)**

Since the results of the regression model depend on these statistical assumptions, the 
results are only correct of our assumptions hold (at least approximately).

Using the fitted model above with the prestige data, answer the following questions

1. Use the **Goldfeld-Quandt** test (`sm.stats.diagnostic.het_goldfeldquandt`) to 
   assert the homoscedasticity of the residuals

2. Use the **Jarque-Bera/Omnibus** test (included in model summary) to assert to the 
   normality of the residuals. 
     
3. Use the **Condition Number** (included in model summary) to assert the lack of multicollinerity.
   As a rule of thumb, a condition number > 30 indicates multicollinearity between the features.
   
   Furthermore, we can use the **Variance Inflation Factor (VIF)** 
   (`sm.stats.outliers_influence.variance_inflation_factor`) to measure how collinear a particular 
   feature is with the rest of the features. As a rule of thumb, a VIF > 10 indicates the feature is
   collinear with at least another feature.
   
   **Hint:**
   - `variance_inflation_factor` takes a matrix of features and the column index of the feature the VIF
     is to be calculated
   - Write a function that loops through and calculate VIF for all the features
   
## Part 2: Interpreting the residuals 

1. Plot studendized residuals (residual divided by standard deviation of residuals)
   on the y axis and each of the following as the x:
   
   - Fitted y value (`Plot A`)
   - Income (`Plot B`)
   - Education (`Plot C`)
   
   **Hint:** 
   - **Use `summary.resid` and `summary.fittedvalues` to get the 
     residuals and the fitted y values**
   - **Use `plotly` to make the plot so the points will be labeled and 
     you can easily refer back to the points with large residuals 
     (`> 2` or `< -2`)**
    - **Below is fitted y values plotted against studendized residuals**
   
   <br>
   
   <div align="center">
      <img width="650" src="images/plotly_resid.png">
   </div>

2. Identify the points with large residuals (more than 2 standard deviations).

3. Influence plot


## Part 3: Partial Regression Plot and Partial Residual Plot

1. 