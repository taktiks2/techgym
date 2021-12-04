import os
from game import *


def main():
    os.system('cls')
    b()  
    show_start_msg()
    set_table()

    while True:
        b()
        show_player_coin()
        bet()
        set_game()
        set_hand_value()
        b()
        show_hand()
        b()

        while not is_stand():
            if is_blackjack():
                show_blackjack_msg()
                b()
                break
            select_action()
            b()
            if is_burst():
                show_burst_msg()
                change_turn()
                b()
                break

        if Game.turn:
            show_dealer_turn_msg()
            b()
            while is_over16():
                hit()
                set_hand_value()
                show_hand()
                b()
                request_enter()
                b()
            if is_blackjack():
                show_blackjack_msg()
                b()
            elif is_burst():
                show_burst_msg()
                b()

        if is_end():
            judge()
        
        if is_no_coin():
            show_no_coin_msg()
            b()
            break
        
        change_turn()
        init_hand()
        init_flags()
        b()
        request_enter()
        os.system('cls')
    

if __name__ == '__main__':
    main()