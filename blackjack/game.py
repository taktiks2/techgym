from player import *
from card import *


class Game:
    PLAYERS: dict = {'player': 0,
                     'dealer': 1}
    SOFT_HAND: int = 0
    HARD_HAND: int = 1
    BLACKJACK: int = 21
    RATE: float = 1.5
    
    deck: Deck = None
    players: list = []
    bet_coin: int = 0
    reward: int = 0
    
    turn: int = 0
    blackjack_flag: bool = False
    player_burst_flag: bool = False
    dealer_burst_flag: bool = False
    stand_flag: bool = False
    end_flag: bool = False


def b():
    print('--' * 25)


def init_flags():
    Game.blackjack_flag = False
    Game.player_burst_flag = False
    Game.dealer_burst_flag = False
    Game.stand_flag = False
    Game.end_flag = False

 
def show_start_msg():
    print('Black Jack')


def set_table():
    Game.deck = Deck()
    for name in Game.PLAYERS:
        Game.players.append(Player(name))


def set_game():
    Game.players[Game.PLAYERS['dealer']].hand.append(Game.deck.deal())
    for _ in range(2):
        Game.players[Game.PLAYERS['player']].hand.append(Game.deck.deal())
    

def bet():
    string = input('コインをベットしてください(1-500): ')
    Game.bet_coin = int(string)


def show_player_coin():
    print(f'持ちコイン: {Game.players[Game.PLAYERS["player"]].coin}')


def hit():
    Game.players[Game.turn].hand.append(Game.deck.deal())


def stand():
    Game.stand_flag = True
    
    
def change_turn():
    Game.turn ^= 1
    

def init_hand():
    for player in Game.players:
        player.hand = []
 

def calc_reward():
    if Game.blackjack_flag:
        Game.reward += Game.bet_coin * Game.RATE
    else: 
        Game.reward = Game.bet_coin


def show_hand():
    for player in Game.players:
        msg = f'{player.name}: '
        for card in player.hand:
            msg += f'{card.name}, '
        print(msg)
        show_values(player)


def show_values(player):
    msg: str = 'value: '
    if player.values[Game.SOFT_HAND] == player.values[Game.HARD_HAND] \
        or player.values[Game.HARD_HAND] > Game.BLACKJACK:
        msg += str(player.values[Game.SOFT_HAND])
    else:
        msg += f'{player.values[Game.SOFT_HAND]} or {player.values[Game.HARD_HAND]}'
    print(msg)


def set_hand_value():
    for player in Game.players:
        for index in range(2):
            player.values[index] = 0
        for card in player.hand:
            if card.number == Number.ACE:
                player.values[Game.SOFT_HAND] += 1
                player.values[Game.HARD_HAND] += 11
            elif card.number.value > 10:
                player.values[Game.SOFT_HAND] += 10
                player.values[Game.HARD_HAND] += 10
            else:
                player.values[Game.SOFT_HAND] += card.number.value
                player.values[Game.HARD_HAND] += card.number.value

        
def is_blackjack():
    for value in Game.players[Game.turn].values:
        if len(Game.players[Game.turn].hand) == 2 and value == Game.BLACKJACK:
            Game.blackjack_flag = True
            return True


def is_burst():
    if Game.players[Game.turn].values[Game.SOFT_HAND] > Game.BLACKJACK:
        if Game.turn:
            Game.dealer_burst_flag = True
        else:
            Game.player_burst_flag = True
        return True


def is_stand():
    if Game.stand_flag:
        return True


def is_over16():
    for value in Game.players[Game.PLAYERS['dealer']].values:
        if value > 16:
            Game.end_flag = True
            return False
        else:
            return True


def is_end():
    if Game.end_flag:
        return True


def select_action():
    string: str = input('ヒットかスタンドを選んでください(H/S): ')
    if string == 'H' or string == 'h':
        hit()
        set_hand_value()
        show_hand()
    elif string == 'S' or string == 's':
        stand()
        change_turn()        


def add_reward():
    Game.players[Game.PLAYERS['player']].coin += Game.reward


def sub_coin():
    Game.players[Game.PLAYERS['player']].coin -= Game.bet_coin


def show_burst_msg():
    print(f'{Game.players[Game.turn].name}はバーストしました')
    if Game.turn:
        Game.end_flag = True


def show_dealer_turn_msg():
    print('dealerのターンです')
    

def show_blackjack_msg():
    print('ブラックジャック')
    Game.end_flag = True


def get_higher_values():
    player_value: int = 0
    dealer_value: int = 0
    for value in Game.players[Game.PLAYERS['player']].values:
        if player_value < value and value <= Game.BLACKJACK:
            player_value = value
    for value in Game.players[Game.PLAYERS['dealer']].values:
        if dealer_value < value and value <= Game.BLACKJACK:
            dealer_value = value
    return player_value, dealer_value


def request_enter():
    input('続けるにはENTERを押してください')

    
def win():
    calc_reward()
    add_reward()
    print('playerの勝ち')
    print(f'{Game.reward}コインを獲得しました')


def lose():
    sub_coin()
    print('dealerの勝ち')


def draw():
    print('引き分け') 


def judge():
    if Game.turn == Game.PLAYERS['player'] and Game.blackjack_flag:
        print('debug: 1')
        win()
    elif Game.turn == Game.PLAYERS['dealer'] and Game.blackjack_flag:
        print('debug: 2')
        lose()
    elif Game.player_burst_flag and Game.dealer_burst_flag:
        print('debug: 3')
        draw()
    elif not Game.player_burst_flag and Game.dealer_burst_flag:
        print('debug: 4')
        win()
    elif not Game.dealer_burst_flag and Game.player_burst_flag:
        print('debug: 5')
        lose()
    else:
        player, dealer = get_higher_values()
        if player == dealer:
            print('debug: 6')
            draw()
        elif player > dealer:
            print('debug: 7')
            win()
        else:
            print('debug: 8')
            lose()
        

def main():
    set_table()
    b()
    
    while True:
        show_player_coin()
        bet()
        set_game()
        set_hand_value()
        b()
        show_hand()
        b()

        # player
        while not is_stand():
            select_action()
            b()
            if is_blackjack():
                calc_reward()
                add_reward()
                show_blackjack_msg()
                break
            if is_burst():
                show_burst_msg()
                sub_coin()
                change_turn()
                break
            
        init_flags()
        
        # dealer
        while is_over16():
            print('debug')
            hit()
            set_hand_value()
            show_hand()
            request_enter()

        if is_end():
            if is_blackjack():
                show_blackjack_msg()
                sub_coin()
            elif is_burst():
                show_burst_msg()
                calc_reward()
                add_reward()
            else:
                judge()

        change_turn()
        init_hand()
        request_enter()


if __name__ == '__main__':
    main()
