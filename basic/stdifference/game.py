from board import *
from validate import *


class Game:
    board: Board = Board()
    LEVELS: dict = {'1': 3,
                    '2': 5,
                    '3': 7,
                    '4': 9,
                    '5': 11,
                    '6': 13,
                    '7': 15,
                    '8': 17,
                    '9': 19} 
    level: str = ''
    epic_coord: str = ''
    coord: str = ''
    continue_flag: bool = None
    promote_flag: bool = None
    clear_flag: bool = None


def b():
    print('--' * 24)


def show_title():
    print('間違い探しゲーム！')


def show_level():
    print(f'レベル{Game.level} スタート！')
    print('違う漢字はどこでしょう？')


def create_board():
    size: int = Game.LEVELS[Game.level]
    Game.board = Board(size, size)
    Game.epic_coord = Game.board.get_epic()


def show_board():
    for row in Game.board.create_rows():
        print(row)


def show_levels_table():
    print('どのレベルから始めますか？')
    for key, index in Game.LEVELS.items():
        print(f'レベル{key}: {index} x {index}')


def select_level():
    max: int = len(Game.LEVELS)
    while True:
        string: str = input(f'レベルを選択してください(1-{max}): ')
        if valid_decimal(string):
            if 1 <= int(string) <= max:
                break
        print(f'※ 1-{max}の整数で入力してください')

    Game.level = string


def promote_level():
    if int(Game.level) < len(Game.LEVELS):
        Game.level = str(int(Game.level) + 1)
    else:
        Game.clear_flag = True


def select_coord():
    while True:
        string_list: list = []
        string: str = input(f'座標値を入力してください(例:A1): ')
        if valid_count(string, 2):
            string_list = string
            if valid_alpha(string_list[0]) and valid_decimal(string_list[1]):
                string = string_list[0].upper() + string_list[1]
                break
        if valid_count(string, 3):
            string_list = string
            if valid_alpha(string_list[0]) and valid_decimal(string_list[1] + string_list[2]):
                string = string_list[0].upper() + string_list[1] + string_list[2]
                break
        print('※ 2-3文字の英数字で入力してください(例:A1)')
                
    Game.coord = string


def show_result():
    results: list = ['正解', '不正解']
    if Game.coord == Game.epic_coord:
        print(f'判定: 正解です！')
        Game.promote_flag = True
    else:
        print(f'判定: 残念、不正解です...')
        print(f'　　　正解は「{Game.epic_coord}」でした')
        Game.promote_flag = False
        

def select_continue():
    '''ゲームを続けるかどうかの判定
    '''
    msg: str = ''
    if is_promote():
        msg += '次のレベルを'
    else:
        msg += '続けて'
    while True:
        string = input(msg + 'プレイしますか？(Y/N): ')
        if valid_count(string, 1):
            if valid_alpha(string):
                upper: str = string.upper()
                if upper == 'Y' or upper == 'N':
                    break
        print('※「Y」か「N」で入力してください')
    if upper == 'Y':
        Game.continue_flag = True
    else:
        Game.continue_flag = False


def is_continue():
    if Game.continue_flag:
        return True
    return False


def is_promote():
    if Game.promote_flag:
        return True
    return False


def is_clear():
    if Game.clear_flag:
        return True
    return False


def show_clear_msg():
    print('ゲームクリア！')


def show_end_msg():
    print('See you again!')


def main():
    Game.level = '5'
    promote_level()
    print(Game.level)


if __name__ == '__main__':
    main()
