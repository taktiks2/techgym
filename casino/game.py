import random
from tools.drawing import border
from tools.validate import valid_integer


class Setting:
    INITIAL_COIN: int = 500
    MAX_BET: int = 99
    NAME: list = ['MY',
                  'C1',
                  'C2',
                  'C3']    
    players: list = []


class Player:
    
    def __init__(self, name: str, coin: int):
        self.name: str = name
        self.coin: int = coin
    
    def info(self):
        print(f'{self.name} : {self.coin}')
    
    def set_bet_coin(self, bet_coin: int):
        self.coin -= bet_coin


class Human(Player):
    
    def __init__(self, name: str, coin: int):
        super().__init__(name, coin)
        self.bet_coin: int = 0
    
    def bet(self):
        max: int = self.coin if self.coin < 99 else Setting.MAX_BET
        while True:
            string: str = input(f'何枚BETしますか？(1-{max}): ')
            if valid_integer(string, Setting.MAX_BET):
                self.bet_coin: int = int(string)
                break
            border()
        super().set_bet_coin(self.bet_coin)


class Computer(Player):
    
    def __init__(self, name: str, coin: int):
        super().__init__(name, coin)
        self.bet_coin: int = 0
    
    def bet(self):
        max: int = self.coin if self.coin < 99 else Setting.MAX_BET
        self.bet_coin: int = random.randint(1, max)
        super().set_bet_coin(self.bet_coin)
