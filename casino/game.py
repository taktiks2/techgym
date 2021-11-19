from player import *
from cell import *
from tools.drawing import border


class Game:
    players: list = []
    bet_table: dict = {}
    player_bets: dict = {}


def create_players():
    '''プレイヤー1人とコンピューター3人のリストを作成
    [Human, Computer, Computer, Computer]
    '''
    for name in Player.NAMES:
        if name == Player.NAMES[0]:
            Game.players.append(Human(name, Player.INITIAL_COIN))
        else:
            Game.players.append(Computer(name, Player.INITIAL_COIN)) 


def show_players():
    '''プレイヤーを表示
    '''
    for player in Game.players:
        player.info()


def init_bet_table():
    '''ベット表を初期化
    '''
    for row in Cell.NAMES:
        bets: dict = {}
        for col in Player.NAMES:
            bets[col] = 0
        Game.bet_table[row] = bets
     
    
def update_bet_table(player_bets: dict):
    '''ベット表をアップデート'''
    index: int = 0
    for place, coin in player_bets.items():
        Game.bet_table[place][Player.NAMES[index]] = coin
        index += 1
        

def show_bet_table():
    '''ベット表を表示
    '''
    border: str = coloring(Cell.COLORS[2], '|')
    # 行題目を作成
    bet_names: list = [border + ' _____ ' + border,]
    red_flag: int = 0
    create_table()
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
        bet_names[0] += f' {name} ' + border
    row: int = 1
    for value in Game.bet_table.values():
        for index in range(len(Player.NAMES)):
            bet_names[row] += f' {str(value[Player.NAMES[index]]).zfill(2)} ' + border
        row += 1
    # 表を描画
    for row in bet_names:
        print(row)
        

def bet_phase():
    '''ベット処理
    '''
    init_bet_table()
    show_bet_table()
    for player in Game.players:
        player.bet()
        print(f'{player.name}は {player.bet_coin}コイン を「{player.bet_place}」にBETしました。')
        Game.player_bets[player.bet_place] = player.bet_coin
    update_bet_table(Game.player_bets)
    show_bet_table()

def main():
    create_players()
    bet_phase()

if __name__ == '__main__':
    main()