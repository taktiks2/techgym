import numpy as np
import scipy.linalg as linalg
import scipy.integrate as integrate
from IPython.core.display import display


def sample1():
    '''行列計算
    '''
    matrix = np.array([[1, -1, -1],
                       [-1, 1, -1],
                       [-1, -1, 1]])
    display(matrix)

    print('行列式')
    display(linalg.det(matrix))
    
    print('逆行列')
    display(linalg.inv(matrix))
    
    display(matrix @ linalg.inv(matrix))

    eig_value, eig_vector = linalg.eig(matrix)
    
    print('固有値')
    display(eig_value)
    print('固有ベクトル')
    display(eig_vector)
    

def sample2():
    '''積分計算
    '''
    function: str = f'2*x*x + 5*x + 4'
    
    result, err = integrate.quad(lambda x: eval(function), 0, 15)
    print(f'f = {function}')
    print(f'積分:{result} 誤差:{err}')


if  __name__ == '__main__':
    #sample1()
    sample2()