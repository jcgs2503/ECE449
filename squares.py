import numpy
import torch

## You only need to complete the two functions.
def numpy_squares(k):
    """return (1, 4, 9, ..., k^2) as a numpy array"""
    # your code here
    return numpy.arange(1,k+1)**2

def torch_squares(k):
    """return (1, 4, 9, ..., k^2) as a torch array"""
    # your code here
    return torch.arange(1,k+1)**2