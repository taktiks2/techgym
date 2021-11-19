import os
from game import *
from tools.drawing import border


def main():
    os.system('cls')
    create_players()
    border()
    show_players()
    border()
    bet_phase()
    border()


if __name__ == '__main__':
    main()