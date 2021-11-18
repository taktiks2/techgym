import phase
from tools.drawing import border


def main():
    phase.create_players()
    border()
    phase.show_players()
    border()
    phase.bet_phase()
    border()


if __name__ == '__main__':
    main()