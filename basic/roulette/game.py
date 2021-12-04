from player import *
from cell import *
from tools.drawing import border


class Game:
    players: list = []  # プレイヤーとコンピューターのインスタンスリスト
    bet_table: dict = {}  # {player.name: {'place': place, 'bet': coin}}
    winners: list = []
    defeated_player: list = []
    hit_pocket: str = ''

def create_players():
    '''プレイヤー1人とコンピューター3人のリストを作成
    [Human, Computer, Computer, Computer]
    '''
    for name in Player.NAMES:
        if name == Player.NAMES[0]:
            Game.players.append(Human(name, Player.INITIAL_COIN))
        else:
            Game.players.append(Computer(name, Player.INITIAL_COIN)) 


def init_bet_table():
    '''ベット表を初期化
    '''
    for row in Cell.NAMES:
        bets: dict = {}
        for col in Player.NAMES:
            bets[col] = 0
        Game.bet_table[row] = bets
     
    
def update_bet_table():
    '''ベット表をアップデート'''
    for player in Game.players:
        Game.bet_table[player.bet_place][player.name] = player.bet_coin
        

def show_bet_table():
    '''ベット表を表示
    '''
    border: str = coloring(Cell.COLORS[2], '|')
    # 行題目を作成
    bet_names: list = [border + ' _____ ' + border,]
    red_flag: int = 0
    for cell in Cell.table:
        string: str = f' {cell.name}(x{cell.rate}) '
        colored_string: str = ''
        if red_flag == 0:
            colored_string = coloring(Cell.COLORS[0], string)
        else:
            colored_string = string
        bet_names.append(border + colored_string + border)
        red_flag ^= 1
    # 表の数値を入力
    for name in Player.NAMES:
        bet_names[0] += f'  {name} ' + border
    row: int = 1
    for value in Game.bet_table.values():
        for index in range(len(Player.NAMES)):
            num: str = str(value[Player.NAMES[index]]).zfill(3)
            if not num == '000':
                colored_num: str = coloring(Cell.COLORS[3], num)
                bet_names[row] += f' {colored_num} ' + border
            else:
                bet_names[row] += f' {num} ' + border
                
        row += 1
    # 表を描画
    for row in bet_names:
        print(row)


def set_bet_coin():
    for player in Game.players:
        player.bet()


def show_bet_coin():
    for player in Game.players:
        print(f'{player.name}は {player.bet_coin}コイン を「{player.bet_place}」にBETしました。')


def set_hit_pocket():
    '''当たりを設定
    '''
    Game.hit_pocket = random.choice(Cell.NAMES)


def show_hit_pocket():
    print(f'選ばれたのは「{Game.hit_pocket}」')


def set_winner():
    '''当たりプレイヤーの判定
    '''
    for player in Game.players:
        if player.bet_place == Game.hit_pocket:
            Game.winners.append(player)


def get_rate():
    if Game.hit_pocket == Cell.NAMES[0] \
        or Game.hit_pocket == Cell.NAMES[1]:
        return Cell.RATES[0]
    else:
        return Cell.RATES[1]


def calc_winning_coin(bet_coin: int):
    rate: int = get_rate()
    return bet_coin * rate


def set_winning_coin():
    for winner in Game.winners:
        winning_coin: int = calc_winning_coin(winner.bet_coin)
        winner.winning_coin = winning_coin
        winner.get_coin(winning_coin)
        
def show_winners():
    if len(Game.winners) == 0:
        print('当たったプレイヤーはいませんでした')
    else:
        for winner in Game.winners:
            print(f'{winner.name}は当たり {winner.winning_coin} を獲得しました')
            

def show_coin():
    msg: str = '[持ちコイン]'
    for player in Game.players:
        msg += f' {player.name}:{player.coin} /'
    print(msg)

def set_game():
    create_players()
    create_table()


def initialize():
    init_bet_table()
    Game.winners = []
    Game.hit_pocket = ''
    


def play_once():
    '''一回のプレイの流れ
    '''
    show_bet_table()
    border()
    show_coin()
    border()
    
    set_bet_coin()
    show_bet_coin()
    border()
    
    update_bet_table()
    show_bet_table()
    border()
    
    set_hit_pocket()
    show_hit_pocket()
    border()
    
    set_winner()
    set_winning_coin()
    show_winners()
    border()
    
    show_coin()
    border()


def is_game_end():
    for player in Game.players:
        if player.coin <= 0:
            Game.defeated_player.append(player)
    
    if len(Game.defeated_player) == 0:
        return False
    return True
    

def game_end():
    msg: str = ''
    if len(Game.defeated_player) == 1:
        msg += Game.defeated_player[0].name
    else:
        for index, player in enumerate(Game.defeated_player):
            if index == len(Game.defeated_player):
                msg += player.name
            else:
                msg += player.name + 'と'
    msg += 'のコインが無くなったためゲームを終了します'
    print(msg)


def main():
    create_players()


if __name__ == '__main__':
    main()
