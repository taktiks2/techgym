import pandas as pd
from urllib import request
from IPython.core.display import display
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    
    DATA = 'adult+stretch.data'
    TXT = 'balloons.names'
    feature: list = ['color', 'size', 'act', 'age', 'inflated']

    def sample1():
        data = 'http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data'
        request.urlretrieve(data, './adult+stretch.data')
        balloons = pd.read_csv(DATA)
        
        txt = "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/balloons.names"
        request.urlretrieve(txt, './balloons.names')
        
        with open(TXT, encoding='utf-8') as f:
            for row in f:
                print(row, end='')
                
        balloons.columns = feature

        display(balloons.info())
        display(balloons)
    
    def sample2():
        balloons = pd.read_csv(DATA)
        balloons.columns = feature
        display(balloons)
        
        display(pd.crosstab(balloons['color'], balloons['size']))
        
        plt.figure(figsize=(10, 10))
        
        plt.subplot(2, 2, 1)
        sns.countplot(x='color', data=balloons)

        plt.subplot(2, 2, 2)
        sns.countplot(x='color', hue='age', hue_order=['CHILD', 'ADULT'], data=balloons)

        plt.subplot(2, 2, 3)
        sns.countplot(x='color', hue='size', hue_order=['SMALL', 'LARGE'], data=balloons)

        plt.show()
                
        
    sample2()
     
if __name__ == '__main__':
    main()
    