import numpy as np
from IPython.core.display import display


def sample1():
    sample: list = [9, 2, 3, 4, 10, 6, 7, 8, 1, 5]

    array1 = np.array(sample)
    print(array1)
    print(array1.shape)
    print(f'次元数: {array1.ndim}')
    print(f'要素数: {array1.size}')
    print(f'掛け算: {array1 ** 2}')
    print(f'累乗: {array1 ** 3}')
    print(f'割り算: {array1 / 2}')

    array1.sort()
    print(f'ソート後: {array1}')
    print(f'ソート後: {array1[::-1]}')
    print(f'Min: {array1.min()}')
    print(f'Max: {array1.max()}')
    print(f'Sum: {array1.sum()}')
    print(f'Cum: {array1[::-1].cumsum()}')
    print(f'Ratio: {array1.cumsum() / array1.sum()}')
    

def sample2():
    array1: np.array = np.linspace(2, 3, 9)
    display(array1, '\n')

    array2 = np.arange(9).reshape(3, 3)
    display(array2, '\n')
    display(array2[0], '\n')
    display(array2[:,0], '\n')

    array3 = np.arange(9, 18).reshape(3, 3)
    display(array3, '\n')
    display(array2 * array3, '\n')
    display(array2 @ array3)
    


if __name__ == '__main__':
    #sample1()
    sample2()
