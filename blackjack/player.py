from PIL.Image import init
from card import *
import numpy as np


class Settings:
    INITIAL_COIN: int = 500


class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.values = [0, 0]
        self.coin = Settings.INITIAL_COIN


def main():
    pass


if __name__ == '__main__':
    main()
