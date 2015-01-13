##Linear Algebra

First part of this exercise gives you some practice of matrix multiplication.

Markov Process, Stochastic Matrix

Suppose that the 2004 state of land use in a city of 60 mi^2 of built-up area is

C: Commercially Used 25%
I: Industrially Used 20%
R: Residentially Used 55%

Find the states in 2009 and 2014, assuming that the transition probabilities for 5-year intervals are given by the matrix **A** and remain practically the same over the time considered.

![](images/transition_matix_A.png)

Note: **A** is a stochastic matrix, that is, a square matrix with all entries nonnegative and all column sums equal to 1. Our example concerns a Markov process,1 that is, a process for which the probability of entering a certain state depends only on the last state occupied (and the matrix **A**), not on any earlier state.



For this part of the exercise we'll use Fisher's Iris data set.

1. Read the [iris](data/iris.txt) dataset into a dataframe.

2. Plot the sepal width vs sepal lenght. For the rest of the exercise, we'll use only these two features.

3. Construct a data matrix using sepal width and sepal length.

4. Calculate the mean vector from the data matrix and plot it along with all the data points.

5. Obtain mean-centered data by subtracting mean vector from each data point.

6. Write a function to calculate the distance between two vectors. Use this to calculate the distance of every point from the mean vector. Plot the histogram of the distances.

7. Write a function to calculate the cosine similarity between two vectors. Calculate the cosine similarity of each point w.r.t the mean vector. Plot histogram of the cosine similarities.

8. Write a function to calculate projection of one vector onto another vector. Use this function to calculate the projections of every point (using centered data) onto vector (1,1). Plot these projections along with the actual data points.

9. Now calculate the projections of all data points (using centered data) onto the vector (-1,1). Plot these projections. How do these projections differ from the previous one.
