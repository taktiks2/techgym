def open_csv(path: str):
    '''指定されたパスのcsvファイルを開く
    各行の最初の値をキーにした辞書を返す

    例)
    A,B,C,D
    E,F,G,H
    ↓
    dict = {'A': ['B', 'C', 'D'],
            'E': ['F', 'G', 'H]'} 

    return: dict
    '''
    csv_file = {}
    with open(path, encoding='utf-8') as f:
        for row in f:
            column = row.rstrip().split(',')
            csv_file[column[0]] = [column[index] for index in range(len(column))]
            
    return csv_file