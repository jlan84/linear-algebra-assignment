Linear Algebra
====================================

1. What is Linear Algebra?
2. Matrices vs Vectors/Notation
3. Scalar Operations
4. Elementwise Operations
5. Matrix Multiplication
6. Identity Matrix
8. Inverse/Determinant
9. Rank


What is Linear Algebra?
==============================

Linear algebra is about being able to solve systems of equations in an efficient manner.

Let's start with a basic example of an equation:

   4 x 1 - 5 x 2 = -13
   
   -2 x 1 + 3 x 2 = 9


If we think of `Ax = b`

Let's change this to matrices:

   A =  4 -5    
       -2  3
   
   b = -13 
         9

Solving this by hand can take a long time. With matrices, there are a lot of established rules of math that come in to play that allows us to do computations efficiently.


Matrices vs Vectors
=====================================
Matrices are a 2d brick of numbers. Vectors are a 1d matrix.

Here is an example matrix
![alt text](https://raw.githubusercontent.com/zipfian/linear-regression/master/images/matrix.jpg?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL21hdHJpeC5qcGciLCJleHBpcmVzIjoxNDAxNTgzODY1fQ%3D%3D--4e9ba8abe5faeb2c51f35daa12860bc58e1b0f02 "Matrix")

2 kinds of vectors, row and column. A row vector is a 1 x n vector where n is the number of columns. A column vector is an m x 1 vector where m is the number of rows. They are transposes of each other (review of that coming up).

Pictured below:
![alt text](
https://raw.githubusercontent.com/zipfian/linear-regression/master/images/vector.jpg?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL3ZlY3Rvci5qcGciLCJleHBpcmVzIjoxNDAxNTg0MDkxfQ%3D%3D--b8918e8202cabbf3aa8f630b420f21e23e9c8844 "Vector")

We can think of matrices and vectors as numerical primitives very similar to scalars (single numbers)

With that being the case, we can do various operations on them. 

The core idea of matrices and vectors is the ability to run numerical routines on large swathes of numbers at once in a fast fashion. This includes being able to operate on several blocks at once in parallel.

A bit of notation: `A^T` (or `A'`) is `A` trasnpose. This flips the columns and rows of the matrix. A quick example:

   A = 0.12974   0.89463   0.63577   0.53814
      
       0.17083   0.10324   0.25069   0.90543
      
       0.30377   0.70167   0.48267   0.35946
   
   
   A' = 0.12974   0.17083   0.30377
      
        0.89463   0.10324   0.70167
      
        0.63577   0.25069   0.48267
      
        0.53814   0.90543   0.35946

Scalar Operations
==================================
Matrices can actually have a  number applied element wise to each. This is called a scalar operation.

In python and other languages, a scalar (again: single number) is typically represented as a scalar matrix.

Example being:

    [2]
    
A scalar matrix is a 1 x 1 matrix that can then typically be blended with any matrix operations natively.

A quick example:


  2 3 5       
  4 5 6              

+ 1 

= 



  3 4 6       
  5 6 7                 




For all intents and purposes a matrix A, scalar matrix B, and scalar x where x is the only element in the 
matrix B are the following:

A + B = A + x


This rule applies to all operations involving a scalar matrix.


Elementwise operations
=======================================


For any matrix A or B, an element wise operation on a matrix can only happen when the matrices are the same shape.

With that assumption:

Let f(A,B) be a transformation over the elements i,j and A and B, and Y be a result of f(A,B):

Y_i,j = f(A_i,j,B,i,j)


An example:
A       B
[       [
[2,2]  [1,1]
[3,3]  [2,2]
]       ]


A + B =   

[
[3,3]
[5,5]
]


Matrix Multiplication
===================================


Different from element wise matrix multiplication, a matrix matrix multiply can only happen

when the columns of the first matrix are the same as the rows of the second matrix. 


Let's identify sub operations of a matrix multiply. This can help contextualize the general case.

#Inner Product/Dot Product

An Inner product, or dot product is as follows:

![alt text](https://raw.githubusercontent.com/zipfian/linear-regression/master/images/dotproduct.png?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL2RvdHByb2R1Y3QucG5nIiwiZXhwaXJlcyI6MTQwMTU5MjMzNn0%3D--989f49147a32d3a2ee1967153f3325d7c74e1952 "Dot Product")

Of note here is that x is a row vector and y is a column vector.



#Outer product


![alt text](https://raw.githubusercontent.com/zipfian/linear-regression/master/images/outerproduct.png?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL291dGVycHJvZHVjdC5wbmciLCJleHBpcmVzIjoxNDAxNTkyMzE1fQ%3D%3D--3f4758bb7c141c3195488d84a222545e445f1f5a "Outer product")


Of note here is that x is a column vector and y is a row vector.






Matrix - Matrix multiply
====================================

A matrix multiply is as follows:


![alt text](https://raw.githubusercontent.com/zipfian/linear-regression/master/images/matrixmultiply.png?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL21hdHJpeG11bHRpcGx5LnBuZyIsImV4cGlyZXMiOjE0MDE1ODY3NDN9--fff76efaa12f548caf71d26e5fa0e51dab69b50a "Matrix Multiply")




A readable version of this: for each i,j in your matrix that will be the number of columns in the first x number of rows in the second, Multiply the row of the first matrix by the column of the second and sum over all the results to form an individual cell where the current row or column is i,j.




We can think of a matrix multiply as a series of vector-vector products. That is that the (i, j)th entry of an output C is equal to the inner product of the ith row of A and the jth column of B.
Symbolically, this looks like the following:


![alt text](https://raw.githubusercontent.com/zipfian/linear-regression/master/images/matrixmultiply2.png?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL21hdHJpeG11bHRpcGx5Mi5wbmciLCJleHBpcmVzIjoxNDAxNTkyOTAwfQ%3D%3D--84c0b404d7837dccfac0b105fa22d18763945b29 "Matrix Multiply form")


Let's do a quick example:

A =

   0.84095   0.97642
   
   0.31362   0.20194



B =

   0.79569   0.26022
   
   0.36514   0.41348


A * B = 

   1.02566   0.62256
   
   0.32328   0.16511


A .* B = 

   0.669134   0.254082
   
   0.114515   0.083497


Notice how the 2 are different. A matrix matrix multiply is applying columns to rows. An element wise is element by element and must be the same size.



Identity Matrix
==================================

An identity matrix is a matrix with all 1s on the diagonal zeros everywhere else.

That is: 


I_i,j = { 1 if i = j, 0 otherwise}



Below is an example identity matrix:

A =


   1   0   0
   
   0   1   0
   
   0   0   1



Identity matrices are used in several different properties of a matrix, the most notable being the inverse.


Rank
=========================


Rank is about finding dependent rows and columns in a matrix. A dependent row or column is a a row or column that trends with another row or column.

An example of this would be a column or row that is merely the multiple of another.

Rank is the number of linearly independent rows or columns in a matrix.


Formalizing this a bit:


![alt text](https://raw.githubusercontent.com/zipfian/linear-regression/master/images/linearindependence.png?token=1144306__eyJzY29wZSI6IlJhd0Jsb2I6emlwZmlhbi9saW5lYXItcmVncmVzc2lvbi9tYXN0ZXIvaW1hZ2VzL2xpbmVhcmluZGVwZW5kZW5jZS5wbmciLCJleHBpcmVzIjoxNDAxNTkzNTgxfQ%3D%3D--21fb966350a8ca000f820d4fa197562ffae7267d "Linear independence")


For any matrix A ∈ R m×n, the row or column rank is the largest subset of rows or columns that are linearly independent.

The following are some basic properties of the rank:
• For A ∈ R m×n , rank(A) ≤ min(m, n). If rank(A) = min(m, n), then A is said to be full rank.

• For A ∈ R m×n , rank(A) = rank(A^T).

• For A ∈ R m×n , B ∈ R n×p , rank(AB) ≤ min(rank(A),rank(B)).

• For A, B ∈ R m×n , rank(A + B) ≤ rank(A) + rank(B)


Inverse and Deterimanant
==================================

An inverse of a matrix is defined as follows:

A^−1 .* A = I = A .* A^−1




A matrix that has an inverse is called invertible.

In order for a square matrix A to have an inverse A^−1, then A must be full rank







