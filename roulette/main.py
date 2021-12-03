import os
from game import *


def main():
    os.system('cls')
    set_game()
    
    while True:
        initialize()
        play_once()
        if is_game_end():
            game_end()
            input('ゲームを終了するにはEnterを押してください')
            break
        input('ゲームを続けるにはEnterを押してください')
        os.system('cls')
    
    os.system('cls')
    

if __name__ == '__main__':
    main()
