import numpy as np
import matplotlib.pyplot as plt

def iterate(z0, its, c_n):

    '''
    Iterates a complex number computation based on an initial complex number and one other fixed complex number.
    Also gives the number of iterations performed before the computed number diverges to infinity if it does.

    Parameters
    ----------

    z0 : float
         initial complex number from which the iteration starts

    its : integer
          number of iterations to be performed

    c_n : float
          complex number involved in the computation


    Returns
    -------

    norm : float
           norm of the final complex number from the iteration. If z diverges, norm = infinity

    nsteps : float or None
             number of iterations before z diverges to infinity. If z does not diverge, nsteps = None

    '''

    z = np.zeros(its+1)
    z[0] = z0

    for i in range(its):

        z[i+1] = (z[i])**2 + c_n

        if z[i+1] == np.inf:
            norm = np.inf
            nsteps = i+1
            return norm, nsteps
            break

    if z[-1] != 0:
        norm = (z[-1].real)**2 + (z[-1].imag)**2
        nsteps = None
        return norm, nsteps



def booling(x, y, res_iter):
    
    '''
    Takes an array and maps each of its values 
    to True if said value is not infinity and 
    to False if said value is infinity
    
    Parameters
    ----------
    
    x : array_like
        dimensional axis over which the iteration from iterate() is analyzed over
        
    y : array_like
        dimensional axis over which the iteration from iterate() is analyzed over
    
    res_iter : array_like
               array of values to be mapped to True or False. Must be of dimension NxM for N = len(x) and M = len(y)
    
    Returns
    -------
    
    bools : array_like
            array of False and True values mapped from res_iter 
    
    '''
    
    bools = [[0 for j in range(len(y))] for i in range(len(x))]

    for i in range(len(x)):
        for j in range(len(y)):
        
            if res_iter[i][j] != np.inf:
                bools[i][j] = True
            
            if res_iter[i][j] == np.inf:
                bools[i][j] = False
    
    return bools


