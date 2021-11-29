from PIL.Image import init
from card import *
import numpy as np


class Settings:
    INITIAL_COIN: int = 500
    HAND_MAX: int = 5


class Player:
    
    def __init__(self):
        self.hand: list = []
        self.hand_values: list = [0, 0]
        self.coin: int = Settings.INITIAL_COIN


def main():
    pass


if __name__ == '__main__':
    main()