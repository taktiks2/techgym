import random
import enum


class Status:
    MAX_LIFE: int = 3


class Hand(Enum):
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2


class Player:
    
    def __init__(self, name: str):
        self.name: str = name
        self.life: int = Settings.MAX_LIFE
        self.hand: Hand = None
    
    def pon(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()