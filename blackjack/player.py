from PIL.Image import init
from card import *
import numpy as np


class Settings:
    INITIAL_COIN: int = 500

class Player:
    HAND_MAX: int = 5
    
    def __init__(self):
        self.hand = []
        self.coin = Settings.INITIAL_COIN

    def bet(self, coin: int):
        self.coin -= coin
        return coin
    
    def hit(self):
        self.hand.append(Deck.deal())
    
    def stand(self):
        pass
    
    def surrender(self):
        pass
    
    def burst(self):
        pass
    
    def blackjack(self):
        pass
    

class Dealer():
    pass


def main():
    pass


if __name__ == '__main__':
    main()