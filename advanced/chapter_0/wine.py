'''Techgym AI-course chaper0'''
import pandas as pd
from IPython.core.display import display


def main():
    '''main function
    '''
    data = 'wine.data'
    txt = 'wine.names'

    df = pd.read_csv(data)

    with open(txt, encoding='utf-8') as f:
        for row in f:
            print(row)

    display(df.info())


if __name__ == '__main__':
    main()
