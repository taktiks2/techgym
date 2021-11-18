from game import Setting, Human, Computer
from tools.drawing import border


def create_players():
    '''プレイヤー1人とコンピューター3人のリストを作成
    [Human, Computer, Computer, Computer]
    '''
    for name in Setting.NAME:
        if name == Setting.NAME[0]:
            Setting.players.append(Human(name, Setting.INITIAL_COIN))
        else:
            Setting.players.append(Computer(name, Setting.INITIAL_COIN)) 


def show_players():
    '''プレイヤーを表示
    '''
    for player in Setting.players:
        player.info()

def bet_phase():
    '''ベット処理
    '''
    for player in Setting.players:
        player.bet()
        print(f'{player.name}は {player.bet_coin}コイン BETしました。')
    border()
    show_players()
