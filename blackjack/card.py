import numpy as np
from enum import Enum
from image import load_image, show_image


class Suit(Enum):
    HEART = 1
    SPADE = 2
    DIAMOND = 3
    CLUB = 4


class Number(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    SUIT: int = 4
    NUMBER: int = 13
    SUIT_STR: list = ['♥',
                      '♠',
                      '♦',
                      '♣']
    NUMBER_STR: list = ['A',
                        '2',
                        '3',
                        '4',
                        '5',
                        '6',
                        '7',
                        '8',
                        '9',
                        '10',
                        'J',
                        'Q',
                        'K']
    
    def __init__(self, name: str, suit: Suit, number: Number, image):
        self.name = name
        self.suit = suit
        self.number = number
        self.image = image


class Deck:
    MAX: int = Card.SUIT * Card.NUMBER
    card_images: list = []
    
    def __init__(self):
        self.get_images()
        self.cards = np.empty(self.MAX, dtype=Card)
        self.create()
        self.shuffle()
    
    def get_images(self):
        for index in range(self.MAX):
            self.card_images.append(load_image(index))
    
    def create(self):
        index: int = 0
        for suit in range(1, Card.SUIT + 1):
            for number in range(1, Card.NUMBER + 1):
                name = Card.SUIT_STR[suit - 1] + Card.NUMBER_STR[number - 1]
                card = Card(name, Suit(suit), Number(number), self.card_images[index])
                self.cards[index] = card
                index += 1
    
    def shuffle(self):
        np.random.shuffle(self.cards)

    def deal(self):
        card = self.cards[-1]
        self.cards = np.delete(self.cards, -1)
        return card

    
def main():
    deck = Deck()
    print(len(deck.cards))
    print(deck.deal().name)
    print(deck.deal().name)
    print(deck.deal().name)
    print(deck.deal().name)
    print(deck.deal().name)
    print(deck.deal().name)
    print(len(deck.cards))


if __name__ == '__main__':
    main()
