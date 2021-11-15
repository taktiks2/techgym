import random

hands: list = ['グー',
               'チョキ',
               'パー']
results: dict = {'win': '勝ち',
                 'lose': '負け',
                 'draw': 'あいこ'}


def start_message():
    print('じゃんけんスタート')


def get_player_hand():
    while True:
        print('自分の手を入力してください')
        player_hand: str = input(f'0:{hands[0]}, 1:{hands[1]}, 2:{hands[2]}')
        if is_hand(player_hand):
            break
        else:
            print('※ 0から2の数字で入力してください')
    return int(player_hand) 


def get_computer_hand():
    return random.randint(0, 2)


def view_result(hand_diff: int):
    key: str = get_result(hand_diff)
    print(results[key])


def get_hand_name(hand_number: int):
    return hands[hand_number]


def view_hand(player_hand: int, computer_hand: int):
    print(f'プレイヤーの手は {get_hand_name(player_hand)}')
    print(f'コンピューターの手は {get_hand_name(computer_hand)}')


def get_result(hand_diff: int):
    if hand_diff == 0:
        return 'draw'
    elif hand_diff == -1 \
            or hand_diff == -2:
        return 'win'
    else:
        return 'lose'


def is_hand(input_hand: str):
    if input_hand.isdigit():
        if 0 <= int(input_hand) <= 2:
            return True
        else:
            return False
    else:
        return False
    

def play():
    player_hand: int = get_player_hand()
    computer_hand: int = get_computer_hand()
    hand_diff: int = int(player_hand) - computer_hand
        
    view_hand(player_hand, computer_hand)
    view_result(hand_diff)
    
    return get_result(hand_diff)


def main():
    print('----------------------------------')
    start_message()

    while True:
        print('----------------------------------')
        if not play() == 'draw':
            break
    
    print('----------------------------------')
            

if __name__ == '__main__':
    main()