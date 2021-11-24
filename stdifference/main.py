import os
from game import *


def play():
    b()
    show_levels_table()
    select_level()
    b()
    
    create_board()
    show_board()
    select_coord()
    b()
    
    show_result()
    b()


def main():
    os.system('cls')
    show_title()
    while True:
        b()
        play()
        if select_continue():
            os.system('cls')
            continue
        show_end_msg()
        b()
        break


if __name__ == '__main__':
    main()
