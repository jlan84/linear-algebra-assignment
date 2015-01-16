# Numpy

DONT EVER USE A FOR LOPOPPOPPOPOOOOPP !!!!!!!

scipy is a library built on numpy.  so is pandas and scikit learn.  think of scipy as a bunch of functions defined in numpy.

## Gotchas

```
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
```

### arrays of arrays vs. matrices

### Slicing a single row/column

returns a 0 dimensional array.  to get a vector:

```python
arr.shape
arr[:,2:3]
arr[:,2]
arr[:,2:np.newaxis]

arr[:, 2].shape #=> (10,)

arr[:, 2:3].shape #-=> (10,1)

arr[:,2:newaxis]

```

### Axis

arr.shape #=> (10, 4)

axis is the index in shape that goes away. axis= 0 corresponds to arr.shape[0]. axis= 1 corresponds to arr.shape[1]. Across 

### Aggregates 

keepdims or newaxis.  Aggregates get rind of the matrixness of arrays

### Broadcasting

only lower dimension to higher dimension

http://wiki.scipy.org/EricsBroadcastingDoc

### Apply along axis vs. vectorize


