import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance
iris = pd.read_csv('data/iris.txt')
data = iris[['SepalWidth', 'SepalLength']].to_numpy()
print(data.T)

# A = np.array([[.7,.1,0],[.2,.9,.2],[.1,0,.88]])


# B1 = np.array([[.25],[.2],[.55]])
# B2 = np.dot(A, B1)
# B3 = np.dot(A, B2)
# print(B3)

# B1 = np.array([[0],[0],[1]])
# B2 = np.dot(A, B1)
# B3 = np.dot(A, B2).transpose()
# B1T = np.array([[0],[0],[1]]).transpose()
# B2T = np.dot(A, B1).transpose()


# print(B3)
# plt.figure(figsize=(9,3))
# plt.subplot(131)
# plt.bar(['C', 'I', 'R'], B1T[0])
# plt.subplot(132)
# plt.bar(['C', 'I', 'R'], B2T[0])
# plt.subplot(133)
# plt.bar(['C', 'I', 'R'], B3[0])


# plt.show()

def check_vector(v1,col):
    if v1.shape[1] != col:
        return False
    else:
        return True
def compare_vectors(v1, v2):
    if v1.shape != v2.shape:
        return False
    else:
        return True
def euclidean_dist(v1,v2, col):
    euc_dist = 0
    if check_vector(v1,col) and check_vector(v2, col):
        if compare_vectors(v1, v2):
            for i in range(len(v1)):
                euc_dist += (v1[i] - v2[i])**2
        else:
            return 'These vectors are not the same shape'
    else:
        return 'One of these is not a column vector'
    return euc_dist**0.5

v1 = np.array([[1],[2],[3]])
v2 = np.array([[4],[5],[6]])

print(euclidean_dist(v1,v2,1))
print(distance.euclidean(v1,v2))

def cosine_simil(v1,v2,col):
    ABprod = 0
    A = 0
    B = 0
    if check_vector(v1, col) and check_vector(v2, col):
        if compare_vectors(v1, v2):
            for i in range(len(v1)):
                ABprod += v1[i]*v2[i]
                A += v1[i]**2
                B += v2[i]**2
        else:
            return 'These vectors are not the same shape'
    else:
        return 'One of these is not a column vector'
    return ABprod/(A**0.5 * B**0.5)

print(cosine_simil(v1,v2,1))
print(1-distance.cosine(v1,v2))

def matrix_mean(matrix):
    matrix_mean = np.mean(matrix,axis=0,keepdims= True)
    return matrix_mean
print(matrix_mean(data).shape[1])

def distance(matrix, func, row_wise=True):
    if not row_wise:
        data = data.T
    mean_row = matrix_mean(matrix)
    result = np.array([])
    for row in matrix:
        col = row[:, np.newaxis]
        mean_col = mean_row.T
        dist = func(mean_col, col, 1)
        result = np.append(result, dist)
    return result

print(distance(data, cosine_simil).shape)

plt.hist(distance(data, cosine_simil), bins=)
plt.xlabel('Cosine Distance')
plt.title('Cosine Distance')
plt.show()

# print(distance(data, cosine_simil))


