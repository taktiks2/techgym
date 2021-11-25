import os
from game import *


def play():
    show_level()
    b()
    
    create_board()
    show_board()
    select_coord()
    b()
    
    show_result()
    b()


def main():
    os.system('cls')
    
    b()
    show_title()
    b()
    
    show_levels_table()
    select_level()
    b()

    while True:
        play()

        if is_promote():
            promote_level()
        
        if is_clear():
            show_clear_msg()
            b()
            break
        
        select_continue()
        if is_continue():
            os.system('cls')
            continue
        
        show_end_msg()
        b()
        break


if __name__ == '__main__':
    main()
