'''Techgym AI-course chaper0'''
import pandas as pd
from IPython.core.display import display
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model


def main():
    '''main function
    '''
    data = 'wine.data'

    wine = pd.read_csv(data)

    display(wine.info())

    columns_name = ['class', 'Alcohol', 'Malic_acid', 'Ash',
                    'Alcalinity_of_ash', 'Magnesium', 'Total_phenols',
                    'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins',
                    'Color_intensity', 'Hue', '0D280_0D315', 'Proline']
    wine.columns = columns_name
    display(wine)

    def sub_15():
        # ヒストグラム
        plt.hist(wine['Alcohol'])
        plt.xlabel('Alcohol')
        plt.ylabel('[%]')

        # 要約統計量
        display(wine['Alcohol'].describe())

        # 統計的データ分析と可視化
        sns.pairplot(wine[['Alcohol', 'Malic_acid', 'Ash',
                           'Total_phenols', 'Color_intensity']])
    # sub_15()

    def sub_16():
        # 線形回帰インスタンス
        REG = linear_model.LinearRegression()
        # 説明変数
        X = wine.loc[:, ['Alcohol']].values
        # 目的変数
        Y = wine['Color_intensity'].values
        # 予測モデル計算
        REG.fit(X, Y)
        # 回帰係数
        display('回帰係数:', REG.coef_)
        # 切片
        display('切片:', REG.intercept_)
        # 散布図
        plt.scatter(X, Y)
        plt.xlabel('Alcohol')
        plt.ylabel('Color_intensity')
        # 線形回帰直線
        plt.plot(X, REG.predict(X))
    sub_16()

    def sub17():


    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
