# git test

import random
from validate import valid_integer


class Game:
    MAX_BET: int = 99


class Player:
    
    def __init__(self, name: str, coin: int):
        self.name: str = name
        self.coin: int = coin

    def info(self):
        print(f'{self.name} : {self.coin}')


class Human(Player):

    def __init__(self, name: str, coin: int):
        super().__init__(name, coin)
        self.bet_coin: int = 0
    
    def bet(self):
        while True:
            self.bet_coin = int(input(f'何枚BETしますか？(1-{Game.MAX_BET}): '))
            if valid_integer(self.bet_coin, Game.MAX_BET):
                break


def main():
    player1 = Human('takeru', 500)
    player1.info()
    player1.bet()
    print(player1.bet_coin)


if __name__ == '__main__':
    main()