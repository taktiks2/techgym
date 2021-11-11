import random
import string

ROW: int = 6
COLUMN: int = 6
ALPHABETS: list = list(string.ascii_uppercase)
MAX: int = ROW * COLUMN


def start_message():
    '''スタートメッセージの表示
    '''
    print('間違い探しゲーム！')
    print('違う漢字を探してください')


def section_message():
    '''難易度の表示
    '''
    level: int = 1
    print(f'レベル:{level}')


def view_question():
    '''間違い探し表を作成
    表示例: mistake_number = 4
    / | ＡＢＣ
    ー+ーーーー
    1 | 眠眠眠
    2 | 眠眼眠
    3 | 眠眠眠
    '''
    data: list = [['見', '貝'],
                  ['土', '士'],
                  ['眠', '眼'],
                  ['犬', '尤'],]
    mistake_number: int= random.randint(0, MAX - 1)
    index: int = random.randint(0, len(data) - 1)

    print(f'デバッグ:mistake_number = {mistake_number}')
    print(data[index])
    
    # 表を作成
    column_alph: str = ''
    for i in range(COLUMN):
        column_alph += ALPHABETS[i] + ' '
    print('--+-' + ('--' * COLUMN) + '-+')
    print('/ | ' + column_alph + ' |')
    print('--+-' + ('--' * COLUMN) + '-+')
    count: int = 0
    for number in range(ROW):
        row: str = ''
        for _ in range(COLUMN):
            if count == mistake_number:
                row += data[index][1]  # 間違い文字の追加
            else:
                row += data[index][0]  # デフォルト文字の追加
            count += 1
        # IDを1ずつ増やして行を表示
        print(f'{number + 1} | ' + row + ' |')
    print('--+-' + ('--' * COLUMN) + '-+')
        
    return mistake_number


def change_input_number(input_str: str):
    '''入力された座標値を整数値に変換
    input_strにはinput()で取得した文字列が格納されている
    入力値: 'A1'
    Aと1に分けて辞書から対応する整数値を返す
    '''
    column_alph = list(input_str)[0]
    row_num = int(list(input_str)[1]) - 1
    
    # 座標値の辞書を作成
    coordinate: dict = {}
    count: int = 0
    for i in range(COLUMN):
        coordinate[ALPHABETS[i]] = [count + (x * COLUMN) for x in range(ROW)]
        count += 1
    
    return coordinate[column_alph][row_num]


def change_string(number: int):
    '''入力された整数値を座標値に変換
    '''
    coordinate: str = ALPHABETS[number % COLUMN] + str((number // ROW) + 1)
    return coordinate


def is_correct_number(mistake_number: int, input_number: int):
    '''入力された二つの引数が同じ数字かどうか判定
    '''
    if mistake_number == input_number:
        return True
    return False


def view_result(is_correct: bool):
    '''正解 or 不正解の表示
    is_correctのブール値によって表示内容を変更する
    True: '正解'
    False: '不正解'
    '''
    if is_correct:
        print('正解')
    else:
        print('不正解')


def play():
    '''ゲーム進行
    '''
    section_message()
    mistake_number: int = view_question()
    choice: str = input('座標値を入力してください(例:A1): ')
    print(f'デバッグ:choice = {choice}')
    
    input_number: int = change_input_number(choice)
    print(f'デバッグ:input_number = {input_number}')
    
    is_correct: bool = is_correct_number(mistake_number, input_number)
    view_result(is_correct)
    if not is_correct:
        correct_coordinate: str = change_string(mistake_number)
        print(f'正解は {correct_coordinate}')


def main():
    print('----------------------------------------------')
    start_message()
    print('----------------------------------------------')
    play()
    print('----------------------------------------------')


if __name__ == '__main__':
    main()
