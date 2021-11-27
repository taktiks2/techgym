from player import *
from card import *


class Game:
    deck: Deck = None
    player: Player = None


def b():
    print('--' * 20)

 
def show_start_msg():
    print('Black Jack')


def set_game():
    Game.deck = Deck()
    Game.player = Player()
    

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


def bet_player():
    pass


def select_action():
    string: str = input('Select Bet or Stand(B/S): ')
    if string == 'B' or string == 'b':
        Game.player
 

def show_card():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
