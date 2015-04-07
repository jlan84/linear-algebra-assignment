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
     so an intercept can be fitted. Use  `add_constant` in statsmodels**


2. Using numpy, write a function that solves the **normal equation** (below).
   As input your function should take a matrix of features (**x**) and
   a vector of target (**y**). You should return a vector of beta coefficients 
   that represent the line of best fit. Calculate  R<sup>2</sup>. 
   
   <div align="center">
      <img height="30" src="images/normal_equation.png">
   </div>

3. Verify your results using statsmodels. Use the code below as a reference.
   ```python
   import statsmodels.api as sms
   model = sms.OLS(y, x).fit()
   summary = model.summary()
   ```

## Part 1: Interpreting a Linear Regression Model

Using the fitted model above, answer the following questions

1. The linear regression model assumes normality and homoscedasticity of the
   residuals. Plot the fitted y values against the studendized residuals 
   (residual divided by standard deviation of residuals). 
   
   **Hint:** 
   - **Use `summary.resid` and `summary.fittedvalues` to get the 
     residuals and the fitted y values**
   - **Use `plotly` to make the plot so the points will be labeled and 
     you can easily refer back to the points with large residuals 
     (`> 2` or `< -2`)**
   
   <br>
   
   <div align="center" width="200px">
      <img src="images/plotly_resid.png">
   </div>

2. Identify the points with large residuals (more than 2 standard deviations).

   Verify the assumptions of linear regression using the following tests:
   
   - Use the Goldfeld-Quandt test (`sm.stats.diagnostic.het_goldfeldquandt`) to 
     assert the homoscedasticity of the residuals
   - Use the Jarque-Bera/Omnibus test (included in model summary) to assert to the 
     normality of the residuals. 

