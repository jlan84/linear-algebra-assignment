import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

def scatter_plot(ax, x, y, title=None):
    ax.scatter(x,y)
    ax.set_title(title)

def euclidean_distance(v1, v2):
    if v1.shape[1] != 1 and v2.shape[1] != 0:
        print('These should be column vectors.')
    if v1.shape != v2.shape:
        print('These vectors are not the same shape.')
    else:    
        sum = 0
        for i in range(v1.shape[1]):
            sum += (v1[i,0] - v2[i,0])**2

        return np.sqrt(sum)

def cosine_similarity(v1, v2):
    if v1.shape[1] != 1 and v2.shape[1] != 0:
        print('These should be column vectors.')
    if v1.shape != v2.shape:
        print('These vectors are not the same shape.')
    else:   
        s = 0
        s1 = 0
        s2 = 0 
        for i in range(v1.shape[0]):
            s += v1[i,0]*v2[i,0]
            s1 += v1[i,0]**2
            s2 += v2[i,0]**2
        
        return s/(np.sqrt(s1)*np.sqrt(s2))

def distances(matrix, metric='euclidean'):
    mean_vector = np.mean(matrix, axis= 0)
    dist = []
    if metric == 'euclidean':
        for i in range(matrix.shape[0]):
            accum = 0
            for j in range(matrix.shape[1]):
                    accum += (matrix[i,j]-mean_vector[j])**2
            dist.append(np.sqrt(accum))
    elif metric == 'cosine':
        for i in range(matrix.shape[0]):
            s = 0
            s1 = 0
            s2 = 0
            for j in range(matrix.shape[1]):
                s += matrix[i,j]*mean_vector[j]
                s1 += matrix[i, j]**2
                s2 += mean_vector[j]**2
            dist.append(s/(np.sqrt(s1)*np.sqrt(s2)))
    return np.array(dist)

def create_histogram(ax, v, title, bins):
    ax.hist(v, bins=bins)
    ax.set_title(title)



if __name__ == '__main__':

    iris = pd.read_csv('../data/iris.txt')
    data = iris[['SepalWidth', 'SepalLength']].to_numpy()
    mean_vector = np.mean(data, axis=0)
    print(mean_vector.shape)
    print(data.shape)
    x = data[:,0]
    y = data[:,1]
    # fig, ax = plt.subplots()
    # scatter_plot(ax,x,y)
    # plt.scatter(mean_vector[0], mean_vector[1], s=200, marker ='x', c='red',
    #             linewidths=3, alpha=.4, edgecolors='red')
    # plt.show()
    
    a = np.array([[5],[4]])
    b = np.array([[3],[2]])
    print(euclidean_distance(a,b))
    print(cosine_similarity(a,b))
    print(distance.cosine(a, b))
    cos_sim = distances(data, metric='cosine')
    euc_dist = distances(data)

    fig, axs = plt.subplots(2,1, figsize=(4,6))
    titles = ['Euclidean Distances','Cosine Similarities']
    plots = [euc_dist, cos_sim]
    for title, plot, ax in zip(titles, plots, axs.flatten()):
        create_histogram(ax, plot, title, bins=30)
    
    plt.tight_layout()
    plt.show()