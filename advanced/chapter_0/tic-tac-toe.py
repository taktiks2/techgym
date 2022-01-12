'''Techgym AI-cource chapter0'''
from IPython.core.display import display
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def main():
    '''main function
    '''
    match_data = 'tic-tac-toe.data'
    txt_name = 'tic-tac-toe.names'

    ttt = pd.read_csv(match_data)

    f = open(txt_name, 'r')
    for row in f:
        print(row)
    f.close

    display(ttt.info())

    columns_name = ['top_left', 'top-middle', 'top-right',
                    'middle-left', 'middle-middle', 'middle-right',
                    'bottom-left', 'bottom-middle', 'bottom-right', 'P-N']

    ttt.columns = columns_name

    display(pd.crosstab(ttt['middle-middle'], ttt['P-N']))

    plt.figure(figsize=(10, 10))

    sns.countplot(x='P-N', hue="middle-middle", hue_order=['x', 'o', 'b'], data=ttt)
    plt.show()


if __name__ == '__main__':
    main()
