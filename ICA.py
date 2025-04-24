import numpy as np
# Independent Component Analysis function
def ICA(x, mu, num_components, iters, mode):
    # Random initialization
    W = np.random.rand(num_components, num_components)
    N = np.size(x, 0)

    # phi varies depending on whether the source
    # is expected to be sub-Gaussian or
    # super-Gaussian
    if mode=='superGauss':
        phi = lambda u : 2*np.tanh(u)
    elif mode=='subGauss':
        phi = lambda u : u-np.tanh(u) 
    else:
        print("Unknown mode")
        return W

    for i in range(iters):
        u = W @ x.T # represents the estimated sources
        # the @ operator denotes matrix multiplication
        
        dW = (np.eye(num_components) - phi(u) @ u.T/N) @ W # gradient update based on the selected
        # activation function 𝜙 and the whitened data x 
        
        # Update
        W = W + mu*dW   
    return(W)