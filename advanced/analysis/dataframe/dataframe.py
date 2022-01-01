'''this is practice of dataframe'''
from urllib import request
import pandas as pd
from IPython.core.display import display
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    '''
    main
    '''
    stretch_data = 'adult+stretch.data'
    txt_name = 'balloons.names'
    feature: list = ['color', 'size', 'act', 'age', 'inflated']

    def sample1():
        data = 'http://archive.ics.uci.edu/ml/'\
            'machine-learning-databases/balloons/adult+stretch.data'
        request.urlretrieve(data, './adult+stretch.data')
        balloons = pd.read_csv(stretch_data)
        txt = "http://archive.ics.uci.edu/ml/"\
            "machine-learning-databases/balloons/balloons.names"
        request.urlretrieve(txt, './balloons.names')
        with open(txt_name, encoding='utf-8') as file:
            for row in file:
                print(row, end='')
        balloons.columns = feature

        display(balloons.info())
    sample1()

    def sample2():
        balloons = pd.read_csv(stretch_data)
        balloons.columns = feature
        display(balloons)
        display(pd.crosstab(balloons['color'], balloons['size']))
        plt.figure(figsize=(10, 10))
        plt.subplot(2, 2, 1)
        sns.countplot(x='color', data=balloons)

        plt.subplot(2, 2, 2)
        sns.countplot(x='color', hue='age',
                      hue_order=['CHILD', 'ADULT'], data=balloons)

        plt.subplot(2, 2, 3)
        sns.countplot(x='color', hue='size',
                      hue_order=['SMALL', 'LARGE'], data=balloons)

        plt.show()
    sample2()


if __name__ == '__main__':
    main()
