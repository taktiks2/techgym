import matplotlib.pyplot as plt
import numpy as np
from IPython.core.display import display
import japanize_matplotlib


def practice():
    matrix1 = np.zeros([3, 3, 3], dtype=int)
    matrix2 = np.ones([3, 3, 3], dtype=int)
    
    # ランダムな整数の行列生成
    matrix3 = np.random.randint(0, 180, size=(3, 3))
    
    matrix4 = np.random.randn(20).reshape(5, -1)
    display(matrix3)
    display(np.sin(np.radians(matrix3)))


def prac_plot():
    init_seed = 0
    x_num = 100
    y_num = 100
    x_fig = 10
    y_fig = 10
    
    # seed値設定
    np.random.seed(init_seed)
    
    # 点群描画
    x = np.random.randn(x_num)
    y = np.sin(x) + np.random.randn(y_num)
    plt.figure(figsize=(x_fig, y_fig))
    plt.plot(x, y, 's')
    
    # sin波描画
    x = np.linspace(-5, 5, 100)  # -5から5までを100等分した一次元array
    plt.plot(x, np.sin(x))

    plt.title('タイトル')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    
    plt.show()


def prac_subplots():
    init_seed = 0
    x_num = 100
    y_num = 100
    x_fig = 10
    y_fig = 10
    
    fig, ax = plt.subplots(figsize=(x_fig, y_fig))
    
    np.random.seed(init_seed)
    
    x = np.random.randn(x_num)
    y = np.sin(x) + np.random.randn(y_num)
    ax.plot(x, y, 'r+')
    
    x = np.linspace(-5, 5, 100)
    ax.plot(x, np.sin(x))
    
    ax.set_title('test2')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    plt.show()

    
def prac_subplots_hist():    
    init_seed = 0
    hist_bin = 40
    N = 100000
    x_fig = 20
    y_fig = 6
    
    np.random.seed(init_seed)
    data = np.random.randn(N)
    data = data * 10 + 50
    print(data[0:10])
    
    fig, ax = plt.subplots(figsize=(x_fig, y_fig))
    plt.hist(data, bins=hist_bin, range=(10, 90))
    
    plt.grid(True)
    plt.show()
    
    
    
if __name__ == '__main__':
    #prac_plot()
    #prac_subplots()
    prac_subplots_hist()
