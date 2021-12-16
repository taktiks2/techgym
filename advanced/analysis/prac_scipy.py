import numpy as np
import scipy.linalg as linalg
from IPython.core.display import display


def sample1():
    matrix = np.array([[1, -1, -1],
                       [-1, 1, -1],
                       [-1, -1, 1]])
    display(matrix)


if  __name__ == '__main__':
    sample1()