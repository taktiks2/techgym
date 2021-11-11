import random


def start_message():
    '''スタートメッセージの表示
    '''
    print('違う漢字の番号(例:A1)を入力してください')


def section_message():
    '''難易度の表示
    '''
    level: int = 1
    print(f'レベル:{level}')


def view_question():
    '''間違い探し表を作成する
    表示例: mistake_number = 4
    / | ＡＢＣ
    ー+ーーーー
    1 | 眠眠眠
    2 | 眠眼眠
    3 | 眠眠眠
    '''
    data: list = [['見', '貝'],
                  ['土', '士'],
                  ['眠', '眼']]
    mistake_number: int= random.randint(0, 8)
    index: int = random.randint(0, 2)

    print(f'デバッグ:mistake_number = {mistake_number}')
    print(data[index])
    
    # 表を作成
    print('/ | ＡＢＣ')
    print('ー+ーーーー')
    count: int = 0
    for number in range(3):
        row: str = ''
        for _ in range(3):
            if count == mistake_number:
                row += data[index][1]  # 間違い文字の追加
            else:
                row += data[index][0]  # デフォルト文字の追加
            count += 1
        # IDを1ずつ増やして行を表示
        print(f'{number + 1} | ' + row)

        
def change_input_number(input_str: str):
    ''''''
    row = list(input_str)[0]
    column = int(list(input_str)[1]) - 1
    coordinate: dict = {'A': [0, 1, 2],
                        'B': [3, 4, 5],
                        'C': [6, 7, 8]}
    print(coordinate[row][column])


def play():
    '''ゲーム進行
    '''
    section_message()
    view_question()
    #choice: str = input('例:A1')
    #print(f'デバッグ:choice = {choice}')


def main():
    start_message()
    play()


if __name__ == '__main__':
    #main()
    test = input('test: ')
    change_input_number(test)