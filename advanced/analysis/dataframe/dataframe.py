import pandas as pd
from urllib import request
from IPython.core.display import display



def main():
    
    DATA = 'adult+stretch.data'
    TXT = 'balloons.names'
    
    def sample1():
        data = 'http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data'
        request.urlretrieve(data, './adult+stretch.data')
        balloons = pd.read_csv(DATA)
        
        txt = "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/balloons.names"
        request.urlretrieve(txt, './balloons.names')
        
        with open(TXT, encoding='utf-8') as f:
            for row in f:
                print(row, end='')
                
        feature: list = ['color', 'size', 'act', 'age', 'inflated']
        balloons.columns = feature

        display(balloons.info())
        display(balloons)
    
    def sample2():
        balloons = pd.read_csv(DATA)
        
        
     
if __name__ == '__main__':
    main()
    