from player import *
from card import *


class Game:
    PLAYERS: dict = {'player': 0,
                     'dealer': 1}
    SOFT_HAND: int = 0
    HARD_HAND: int = 1
    BLACKJACK: int = 21
    
    deck: Deck = None
    players: list = []
    bet_coin: int = 0
    
    turn: int = 0
    burst_flag: bool = False
    blackjack_flag: bool = False


def b():
    print('--' * 20)

 
def show_start_msg():
    print('Black Jack')


def set_game():
    Game.deck = Deck()
    for name in Game.PLAYERS:
        Game.players.append(Player(name))
    

def bet():
    string = input('How much coins would you BET?(1-500): ')
    Game.bet_coin = int(string)
    Game.player.coin -= Game.bet_coin
    

def hit():
    Game.player.hand.append(Deck.deal())


def stand():
    Game.turn ^= 1


def surrender():
    pass


def show_hand():
    print()    

def set_hand_value():
    values: list = [0, 0]
    for card in Game.player[Game.turn].hand:
        if card.number == Number.ACE:
            values[Game.SOFT_HAND] += 1
            values[Game.HARD_HAND] += 11
        elif card.number.value > 10:
            values[Game.SOFT_HAND] += 10
            values[Game.HARD_HAND] += 10
        else:
            values[Game.SOFT_HAND] += card.number.value
            values[Game.HARD_HAND] += card.number.value
    return values


def judge_hand_vlaue():
    values: list = set_hand_value()
    for value in values:
        if len(Game.player[Game.turn].hand) == 2 and value == Game.BLACKJACK:
            Game.blackjack_flag = True
        
    
     


def burst():
    pass


def blackjack():
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
    set_game()
    bet()
    
    


if __name__ == '__main__':
    main()
