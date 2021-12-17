import pandas as pd
from IPython.core.display import display
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
    
    pd.set_option('display.unicode.east_asian_width', True)  # 日本語の文字幅に合わせて表を表示する
    df = pd.DataFrame(data)
    display(df, '\n')
    display(df.T, '\n')
    
    new_index = list('ebadcfghij')
    df.index = new_index
    display(df.head(3), '\n')
    display(df.tail(6).loc[:,['性別', '年齢', '勝ち']])


if __name__ == '__main__':
    #sample1()
    sample2()
