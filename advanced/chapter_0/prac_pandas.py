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
    
    id = [str(num) for num in range(100, 110)]
    num = [num for num in range(10)]
    feature_eng = ['gender', 'age', 'win', 'lose', 'draw']
    feature_jap = ['性別', '年齢', '勝ち', '負け', 'あいこ']

    def exp3():
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
    #exp3()
    
    feature_2 = ['address', 'hobby', 'job']
    id2 = ['100', '101', '102', '103', '110', '111', '106', '113', '108', '114']
    address = [random.choice(['東京', '大阪', '愛知', '福岡']) for _ in range(10)]
    hobby = [random.choice(['野球', '賭博', 'じゃんけん']) for _ in range(10)]
    job = [random.choice(['IT', '医療', '事務', '弁護士']) for _ in range(10)]
    data2: dict = {'住所': address,
                   '趣味': hobby,
                   '仕事': job}

    def exp4():
        df_demo: pd.DataFrame = df.copy()
        df_demo.columns = feature_eng
        df_demo.columns.names = ['feature']
        display(df_demo.columns.names)
        df_demo['id'] = id
        display(df_demo)
        df_demo.set_index('id', inplace=True)
        display(df_demo)
        
        df_demo2 = pd.DataFrame(data2)
        display(df_demo2)
        df_demo2.columns = feature_2
        df_demo2.columns.names = ['feature']
        df_demo2['id'] = id
        display(df_demo2)

        df_demo2.set_index('id', inplace=True)
        display(df_demo2)
    #exp4()
    
    def exp5():
        df1 = df.copy()
        df2 = pd.DataFrame(data2)
        
        df1['id'] = id
        display(df1)
        df2['id'] = id2
        display(df2)
        
        display(pd.merge(df1, df2, on='id'))
        display(pd.merge(df1, df2, how='outer', on='id'))
        display(pd.merge(df1, df2, how='left', on='id'))
        display(pd.merge(df1, df2, how='right', on='id'))
    #exp5()
    
    def exp6():
        df1 = df.copy()
        df2 = pd.DataFrame(data2)

        df1.columns = feature_eng
        df1.columns.names = ['feature']
        df1['id'] = id
        df1.set_index('id', inplace=True) 

        df2.columns = feature_2
        df2.columns.names = ['feature']
        df2['id'] = id2
        df2.set_index('id', inplace=True)

        concat_data = pd.concat([df1, df2], sort=True)
        
        display(df1)
        display(df2)
        display(concat_data)   
    #exp6()
    
    def exp7():
        num = ['0','1','2','3','4','5','6','7','8','9']
        add_num = ['10']
        feature =['id','gender','age','address','hobby','job','win','lose','draw']

        hand1 = {'番号'  :['100','101','102','103','104','105','106','107','108','109'],
                '性別'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
                '年齢'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
                '住所'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
                '趣味'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
                '仕事'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
                '勝ち'  :[20,21, 4,60,14,10,12,19,12,14],
                '負け'  :[24,15,35, 3,35,29, 2,12,11,43],
                'あいこ':[15,40,34,29,14, 4,22,17,12,10]}
        hand2 = {'id':['104'],
                'gender':['女性'],
                'age':['40代'],
                'address':['東京'],
                'hobby':['ルーレット'],
                'job':['事務'],
                'win':[14],
                'lose':[35],
                'draw':[14]}
        
        df1 = pd.DataFrame(hand1)
        df1.columns = feature
        df1.columns.names = ['feature']
        df1['NUM'] = num
        df1.set_index('NUM', inplace=True)
        
        df2 = pd.DataFrame(hand2)
        df2.columns.names = ['feature']
        df2.index = add_num
        df2.index.names = ['NUM']
        
        df3 = df1.append(df2)
        
        display(df3)
        display(df3.duplicated())
        display(df3[df3.duplicated()])
        
        df4 = df3.drop_duplicates()
        display(df4)

        display(df4.isnull().sum())
    #exp7()
    
    def exp8():
        hand1 = {'id'  :['100','101','102','103','104','105','106','107','108','109'],
                'gender'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
                'age'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
                'address'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
                'hobby'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
                'job'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
                'win'  :[20,21, 4,60,14,10,12,19,12,14],
                'lose'  :[24,15,35, 3,35,29, 2,12,11,43],
                'draw':[15,40,34,29,14, 4,22,17,12,10]}
        
        df = pd.DataFrame(hand1)
        display(df)
        
        # ビン分割
        draw_bins: list = [1, 10, 20, 30, 40]
        df_draw_bins = pd.cut(df.draw, draw_bins)
        display(df_draw_bins)
        display(pd.value_counts(df_draw_bins))

        # 中央値分割
        df_draw_bins_cut = pd.cut(df.draw, 2)
        display(df_draw_bins_cut)
        display(pd.value_counts(df_draw_bins_cut))
        
        # 均等分割
        df_draw_bins_qcut = pd.qcut(df.draw, 2)
        display(df_draw_bins_qcut)
        display(pd.value_counts(df_draw_bins_qcut))
    #exp8()

    def exp9():
        hand1 = {'id'  :['100','101','102','103','104','105','106','107','108','109'],
                'gender'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
                'age'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
                'address'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
                'hobby'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
                'job'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
                'win'  :[20,21, 4,60,14,10,12,19,12,14],
                'lose'  :[24,15,35, 3,35,29, 2,12,11,43],
                'draw':[15,40,34,29,14, 4,22,17,12,10]}
        
        df = pd.DataFrame(hand1)

        display(df[df.age == '10代'])
        
        display(df.groupby('age').size())
        display(df.groupby('age')['win'].mean())
        display(df.groupby(['age', 'address'])['win'].mean())
    #exp9()

    def exp10():
        hand1 = {'id'  :['100','101','102','103','104','105','106','107','108','109'],
                'gender'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
                'age'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
                'address'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
                'hobby'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
                'job'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
                'win'  :[20,21, 4,60,14,10,12,19,12,14],
                'lose'  :[24,15,35, 3,35,29, 2,12,11,43],
                'draw':[15,40,34,29,14, 4,22,17,12,10]}
        
        df = pd.DataFrame(hand1)
        
        # 単体
        display(df.groupby('age').get_group('10代'))
        
        # 全部
        for group, sub_df in df.groupby('age'):
            display(group)
            display(sub_df)
            display('----------------------')
        
        functions = ['count', 'mean', 'max', 'min']
        grouped_df = df.groupby('age')
        display(grouped_df['win'].agg(functions))
    #exp10()

    def exp11():
        hand1 = {'id'  :['100','101','102','103','104','105','106','107','108','109'],
                'gender'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
                'age'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
                'address'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
                'hobby'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
                'job'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
                'win'  :[20,21, 4,60,14,10,12,19,12,14],
                'lose'  :[24,15,35, 3,35,29, 2,12,11,43],
                'draw':[15,40,34,29,14, 4,22,17,12,10]}
        
        df = pd.DataFrame(hand1)
        
        # csv書き込み
        df.to_csv('df.csv')

        df.iloc[1, 0] = np.nan
        df.iloc[6, 6] = np.nan
        df.iloc[2:4, 2] = np.nan
        df.iloc[5:, 3] = np.nan
        display(df)
        
        # 欠損数
        display(df.isnull().sum())
        # リストワイズ
        display(df.dropna())
        # 0埋め
        display(df.fillna(0))
        # 前の値埋め
        display(df.fillna(method='ffill'))
        # 平均値埋め
        display(df.fillna(df.mean()))
        display(df.mean())
        
        # csv読み込み
        df1 = pd.read_csv('df.csv')
        display(df1)
    exp11()
        

def sample3():
    pass


if __name__ == '__main__':
    #sample1()
    #sample2()
    sample3()
