import numpy as np
import matplotlib.pyplot as plt


def land_use(m, v):
    return np.dot(m,v)

def city_plot(m,v,t,ax, title=None):
    lst = [v]
    v1 = v
    for i in range(t):
        lst.append(np.dot(m,v1))
        v1 = np.dot(m,v1)
    
    t0 = 2004
    x = [t0]
    for i in range(t):
        t0 += t0 + 5
        x.append(t0)
    
    c = [x[0] for x in lst]
    i = [x[1] for x in lst]
    r = [x[2] for x in lst]
    y_values = [c,i,r]
    labels = ['commercial', 'industrial', 'residential']
    for y, l in zip(y_values,labels):
        ax.plot(x, y, label=l)
    
    ax.set_title(title)
    


if __name__ == "__main__":
        

    A = np.array([[0.7,0.1,0],[.2,.9,.2],[.1,0,.8]])

    year_2004 = np.array([[.25],[.2],[.55]])
    year_2009 = land_use(A,year_2004)
    year_2014 = land_use(A,year_2009)
    # 1
    print(year_2009,'\n', year_2014)

    # 2
    year_2004 = np.array([0,0,1])
    # fig, ax = plt.subplots()
    
    # city_plot(A,year_2004,4, ax)
    # plt.show()

    #3
    all_c = np.array([1,0,0])
    all_i = np.array([0,1,0])
    all_r = np.array([0,0,1])

    # fig, axs = plt.subplots(3,1, figsize=(4,8))

    # plts = [all_c, all_i, all_r]
    # titles = ['Commercial Start', 'Industrial Start', 'Residential Start']

    # for plot, title, ax in zip(plts, titles, axs.flatten()):
    #     city_plot(A, plot, 5, ax, title=title)
    
    # plt.legend()
    # plt.tight_layout()
    # plt.show()