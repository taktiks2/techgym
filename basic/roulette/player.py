import random
from cell import Cell
from tools.drawing import border
from tools.validate import *


class Player:
    INITIAL_COIN: int = 500
    MAX_BET: int = 400
    NAMES: list = ['MY',
                  'C1',
                  'C2',
                  'C3']    

    def __init__(self, name: str, coin: int):
        self.name: str = name
        self.coin: int = coin
        self.bets: dict = {}
    
    def set_bet_coin(self, bet_coin: int):
        self.coin -= bet_coin
    
    def get_coin(self, winning_coin: int):
        self.coin += winning_coin


class Human(Player):
    
    def __init__(self, name: str, coin: int):
        super().__init__(name, coin)
        self.bet_coin: int = 0
        self.bet_place: str = ''
        self.winnning_coin: int = 0
    
    def bet(self):
        max: int = self.coin if self.coin < Player.MAX_BET else Player.MAX_BET
        while True:
            string: str = input(f'何枚BETしますか？(1-{max}): ')
            if valid_integer(string, max):
                self.bet_coin = int(string)
                break
            border()
        super().set_bet_coin(self.bet_coin)
        while True:
            string = input('どこにBETしますか？(R,B,1-8): ')
            upper: str = string.upper()
            if valid_list(upper, Cell.NAMES):
                self.bet_place = upper
                break
            border()


class Computer(Player):
    
    def __init__(self, name: str, coin: int):
        super().__init__(name, coin)
        self.bet_coin: int = 0
        self.bet_place: str = ''
        self.winning_coin: int = 0
    
    def bet(self):
        max: int = self.coin if self.coin < Player.MAX_BET else Player.MAX_BET
        self.bet_coin = random.randint(1, max)
        super().set_bet_coin(self.bet_coin)
        self.bet_place = random.choice(Cell.NAMES)


def main():
    pass


if __name__ == '__main__':
    main()
