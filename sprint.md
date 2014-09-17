Linear Algebra
===================================
In this sprint, we will be doing a numpy focused linear algebra overview.

This will cover all of the basic operations you can do with matrices, as well as some properties of linear algebra with relevant machine learning.

One thing of note, please create a function per exercise. This is to ensure that named clashes from specified names in each function do not interfere with each other.


Overview
==============================
1. Matrix vs Vectors
2. Scalar Operations
3. Matrix Vector Multiplication
4. Matrix Matrix Multiplication
5. Elementwise Matrix Operations
6. Axis wise operations
7. Rank
8. Extra Credit


Resources
====================
* [Linear dependence](http://www.math.oregonstate.edu/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/lindep/lindep.html)
* [Rank](http://www.cliffsnotes.com/math/algebra/linear-algebra/real-euclidean-vector-spaces/the-rank-of-a-matrix)
* [Rank in numpy](http://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.linalg.matrix_rank.html)
* [Determinant in numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html)
* [Broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
* [Matrix overview](http://cs229.stanford.edu/section/cs229-linalg.pdf)
* [Nd arrays](http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)


Matrix Vs Vectors
=====================================
If we remember right, vectors are just 1d matrices.

Use numpy to complete the following tasks.

1. Create a row vector with numpy (1 x some m).
2. Create a column vector with numpy (some n x 1).
3. Create a scalar vector (1 x 1).
4. Create a square 6 by 6 matrix.
5. Create a random 2 x 3 matrix and a random 3 x 2 matrix. You should be able to do this with one command (look at the [numpy random module](http://docs.scipy.org/doc/numpy/reference/routines.random.html)). You can fill it in with integers or real numbers, your choice of the range.
6. Create a 6 x 6 identity matrix.
7. Create a matrix with any values and size and save it as `A`.
8. Get the number of rows and columns of the matrix `A`.
9. Create a transpose of the matrix `A`.
10. Reshape the matrix `A` in to a 1 x n vector, where n is whatever it needs to be for the size of your matrix.


Scalar Operations
==============================
1. Given: 
    
         [2 3 5]

   Do a scalar addition, subtraction, multiply, divide by as separate scalars:
   
          0.5
          -2
           0

2. Given: [4, 5, 6] (scalar matrix)

          0.5
          -2
           0

3. Extra Credit: Vectorize number 1 and 2 and split the matrices out to get the equivalent results. (Broadcasting!)

4. Extra Credit: Given [2] multiply this by a random 2 x 2 pandas dataframe. The output is a numpy array.


Matrix Vector Multiplication
============================================
1. Create a random column vector, row vector, and 3 x 3 square matrix called `column_vector`, `row_vector`, and `rand_matrix` respectively.
2. Perform a vector vector multiply on `column_vector` and `row_vector`. This should output a `n x m` matrix where `n` is the number of rows in `row_vector` and `m` is the number of columns in `column_vector`. Say `column_vector` is a 2 x 1 and `row_vector` is a 1 x 3, output will be a 2 x 3 matrix.
3. For both `column_vector` and `row_vector`, multiply by `rand_matrix`.
4. Compute the dot product of `row_vector` and `column_vector`.
5. Multiply each row of the `rand_matrix` by `row_vector`.
6. If we have a 2 x 3 a 3 x 2, can you matrix multiply them? If so, what is the shape?
7. Taking the output of the resulting matrix from 6, can we matrix multiply a 5 x 6 on that? If so, what is the shape?


Matrix Matrix Multiplication
======================================
1. Create a random 3 x 6 matrix as `rand_matrix`.
2. Matrix multiply `rand_matrix` and the transpose of `rand_matrix`.
3. Reshape `rand_matrix` (create a copy) and matrix multiply it by the original. This should be a 3 x 3.
4. Implement matrix multiply given 2 2-dimensional lists of numbers. Test it out with a 6 x 2 matrix and a 2 x 6 matrix. 


Elementwise Matrix Operations
========================================
1. Create 2 random 6 x 2 matrices as `rand_matrix` and `rand_matrix_2`.
2. Square `rand_matrix` (this will be the same shape).
3. Add, subtract, multiply and divide `rand_matrix` and `rand_matrix_2` (This will be the same shape).
4. Implement element wise multiply given 2 2d lists.
5. Implement dot product given 2 2d lists.


Axis wise operations and operations across different dimensional matrices
================================
1. Create a 4 x 1 random matrix as `rand_matrix`.
2. Create a 1 x 3 random matrix as `rand_matrix_2`.
3. Add the 2 (yes this is possible!) using new axis (this will be a 4 x 3).
4. Create a random 2 x 3 matrix as `rand_matrix`.
5. Calculate the column and row wise sums,mean and standard deviation of the matrix. 
6. Multiply column 1 (0 based indices!) of rand_matrix by 2.


Rank
======================================
1. Create a random 3 x 3 matrix as `rand_matrix`.
2. Add a column to the matrix to make it a 3 x 4 populating it with 2 * the first column.
3. Calculate the rank of the matrix. This should be a number.


Extra Credit 1:
===========================
1. Implement transpose without using the numpy method. Can you do it without using a loop?
2. Implement the reshape function.


Extra Credit (> 2 dimensional data, yes this is used! Look in to tensors) 
===========================
1. Create a random 3d tensor with 2 slices and 3 rows per slice.
2. Sum the 2 slices of the tensor.
3. Create a random 4d tensor with 4 slices, 3 rows per slice, and 2 columns.
4. Add 1 to the first row of each slice of the tensor created in 3.
