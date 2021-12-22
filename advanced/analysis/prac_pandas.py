import pandas as pd
from IPython.core.display import display
import numpy as np
import random

    
def sample1():
    df = pd.Series(['グー', 'チョキ', 'パー'])
    display(df, '\n')
    
    display(df[1], '\n')
    
    display(df.dtypes, '\n')
    
    df_abc = df.copy()    
    df_abc.index = list('abc')
    display(df_abc)
    display(df_abc.index)


def sample2():
    LOOP = 10
    init_seed = 0
    random.seed(init_seed)
    sex = [random.choice(['男性', '女性']) for _ in range(LOOP)]
    age = [random.choice(['10代', '20代', '30代', '40代', '50代']) for _ in range(LOOP)]
    win = [random.randint(4, 70) for _ in range(LOOP)]
    lose = [random.randint(4, 70) for _ in range(LOOP)]
    draw = [random.randint(4, 70) for _ in range(LOOP)]
    data = {'性別': sex,
            '年齢': age,
            '勝ち': win,
            '負け': lose,
            'あいこ': draw}
    
    # 日本語の文字幅に合わせて表を表示する
    pd.set_option('display.unicode.east_asian_width', True)  
    df = pd.DataFrame(data)
    
    def exp1():
        display(df, '\n')
        display(df.T, '\n')
        
        new_index = list('ebadcfghij')
        df.index = new_index
        display(df.head(3), '\n')
        display(df.tail(6).loc[:,['性別', '年齢', '勝ち']])
        
        display(df['性別'] == '女性')
        display(df[df['性別'] == '男性'])
        display(df.drop('年齢', axis=1))
    #exp1()
    
    def exp2():
        display(df.groupby('性別')['勝ち'].mean())
        display(df.groupby('性別')['勝ち'].max())
        display(df.groupby('性別')['勝ち'].min())
        
        display(df['勝ち'].sort_values())
        
        df['あいこ'] = np.nan
        display(df)

        display(df.isnull())
        display(df.isnull().sum())
    #exp2()
    
    def exp3():
        id = [str(num) for num in range(100, 110)]
        num = [num for num in range(10)]
        feature_eng = ['gender', 'age', 'win', 'lose', 'draw']
        feature_jap = ['性別', '年齢', '勝ち', '負け', 'あいこ']
        
        df_copy = df.copy()
        df_copy.index = [id, num]
        display(df_copy)
        display(df_copy.index)
        df_copy.index.names = ['NUM', '番号']
        display(df_copy)
        df_copy.columns = [feature_eng, feature_jap]
        display(df_copy.columns)

        df_copy.columns = df_copy.columns.droplevel(1)
        df_copy.index = df_copy.index.droplevel(1)
        display(df_copy)
        
        display(df_copy['gender'])
        display(df_copy.drop(['106'], axis=0))
        display(df_copy.drop(['gender'], axis=1))
        display(df_copy)
        
    exp3()
    
def sample3():
    pass


if __name__ == '__main__':
    #sample1()
    sample2()
    sample3()
