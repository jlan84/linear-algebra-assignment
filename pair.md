

## Eigenvalue Problems Arising from Markov Processes

Markov processes as considered in morning sprint lead to eigenvalue problems if we ask for the limit state of the process in which the state vector **x** is reproduced under the multiplication by the stochastic matrix **A** governing the process, that is, **Ax** = **x**. Hence **A** should have the eigenvalue 1, and **x** should be a corresponding eigenvector. This is of practical interest because it shows the long-term tendency of the development modeled by the process.

You can find basic introduciton to Markov process ![here](http://austingwalters.com/introduction-to-markov-processes/)

1. Lets reconsider the stochastic matrix from the morning sprint:  
![](images/transition_matix_A.png)  
Find the eigenvector for this matrix corresponding to the eigenvalue of 1.




## PAgeRank for a toy WWW

For this exercise we will be working with a simple network of websites.

![](images/pageweb.png)

In this image, each node corresponds to a web page and each directed edge corresponds to one page referencing the other.  These web pages correspond to the states our Markov chain can be in.  And assume that the model of our chain is that of a random surfer/walker.  

In this model, we transition from one web page (state) to the next with equal probability (to begin).  Or rather we randomly pick an outgoing edge from our current state.  Before we can do any sort of calculation we need to know how we will move on this Markov Chain.  

The PageRank metric actually corresponds to the "stationary distribution" of the chain.  The stationary distribution is the limiting distribution of the Markov chain when iterated.  Or rather the configuration that another iteration/step does not change the probability distribution of our surfer and represents the likelihood that our random surfer is on a page after a very long time of random surfing.  

1. Using numpy, create the transition probabilities in a matrix form for this simple web where position _i_, _j_ in the matrix corresponds to the probability of going from state _i_ to state _j_.  
Now that we have a transition matrix, the next step is to iterate on this from one page to the next (like someone blindly navigating the internet) and see where we end up. The probability distribution for our random surfer can be described in this matrix notation as well (or vector rather)

2. Initialize a vector for the probability of where our random surfer is.  It will be a vector with length equal to the number of pages.  Initialize it to be equally probable to start on any page (i.e. you start randomly in a state on the chain).

3. To take a step on the chain, simply matrix multiple our user vector by the transition matrix.  After one iteration, what is the most likely location for your random surfer?

4. Plot how the probabilities change.  Iterate the matrix through the first ten steps.  At each step create a bar plot of the surfers probability vector. (or if you want to get fancy you can plot everything on one [3 dimensional plot](http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html) by representing time in the z direction)

5. This time to compute the stationary distribution, we can use numpy's matrix operations. Using the function for calculating [eigenvectors](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html) compute the stationary distibution (page rank).  Is it the same as what you found from above?  What is it's eigenvalue?
