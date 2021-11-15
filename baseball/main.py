import random
from operafile import open_csv


class Game():
    INNINGS: int = 9
    PLAYERS: list = ['先攻',
                     '後攻']
    TURN: dict = {'top': 0,
                  'bot': 1}
    MIN_RATE: int = 10
    INPUT_LIST_PATH: str = 'input/teamlist.csv'
    OUTPUT_LIST_PATH: str = 'output/results.txt'


class Team():
    def __init__(self, id_num: int, name: str, attack: int, defense: int):
        self.id_num: int = id_num
        self.name: int = name
        self.attack: int = attack
        self.defense: int = defense
        self.total_score: int = 0
    
    def info(self):
        print(f'{self.id_num} ) {self.name}: 攻撃力:{self.attack} / 守備力{self.defense}')
    
    def get_hit_rate(self):
        '''攻撃力を設定
        '''
        hit_rate: int = random.randint(Game.MIN_RATE, self.attack)
        return hit_rate
    
    def get_out_rate(self):
        '''守備力を設定
        '''
        out_rate: int = random.randint(Game.MIN_RATE, self.defense)
        return out_rate


def create_teams():
    '''Teamインスタンスのリストを作成
    teamlist.csv内の各行にある情報から各チームのインスタンスを作成する
    id_num,name,attack,defense
    return例: [Team(3, '中日ドラゴンズ', 50, 50), Team(2, '阪神タイガース', 30, 70), ・・・]
    '''
    teams: list = []
    team_list: dict = open_csv(Game.INPUT_LIST_PATH)
    
    for status in team_list.values():
        id_num: int = int(status[0])
        name: str = status[1]
        attack: int = int(status[2])
        defense: int = int(status[3]) 
        teams.append(Team(id_num, name, attack, defense))
        
    return teams  # list


def get_inning_scores(playing_teams: dict):
    '''選択されたチーム情報から得点を計算
    return例: [3, 4] ← [top, bot]
    '''
    score: int = 0
    inning_scores: list = [0, 0]
    order: list = list(playing_teams.keys())
    
    # 1イニング分のスコアを計算
    for turn in Game.TURN.values():
        if turn == Game.TURN['bot']:
            order.reverse()  # チェンジ処理
        attack: Team = playing_teams[order[0]]
        defense: Team = playing_teams[order[1]]
        score = (attack.get_hit_rate() - defense.get_out_rate()) // 10
        if score < 0:
            score = 0
        inning_scores[turn] = score
        
    return inning_scores


def border():
    print('----------------------------------------------------------')
    

def main():
    teams: list = create_teams()
    playing_teams: dict = {}
    
    # 各チームごとのステータスの描画
    border()
    print('全チーム情報')
    border()
    for team in teams:
        team.info()
    border()
    
    # チーム選択処理
    for player in Game.PLAYERS:
        id_num: int = int(input(f'{player}のチームを選択して下さい(1-{len(teams)}): ')) - 1
        playing_teams[player] = teams[id_num]
        team_name: str = ''
        if player == Game.PLAYERS[0]:
            attack_first: Team = playing_teams[player]  # 先攻
            team_name = attack_first.name
        else:
            defense_first: Team = playing_teams[player]  # 後攻
            team_name = defense_first.name
        print(f'{player}は「{team_name}」を選択しました')
        border()      
    
    # スコアボードの作成
    score_boards: list = ['____|',
                         f'{Game.PLAYERS[0]}|',
                         f'{Game.PLAYERS[1]}|']
    
    for inning in range(Game.INNINGS):
        inning_scores: dict = get_inning_scores(playing_teams)
        for row in range(len(score_boards)):
            # イニングと合計のコラム作成
            if row == 0:
                score_boards[row] += f' {inning + 1} |'
                if inning == Game.INNINGS - 1:  # 最終回の処理
                    score_boards[row] += " R |"
            # イニングごとの先攻チーム得点を追加
            elif row == 1:
                score = inning_scores[Game.TURN['top']]
                score_boards[row] += f' {score} |'
                attack_first.total_score += score
                if inning == Game.INNINGS - 1:  # 最終回の処理
                    score_boards[row] += f' {attack_first.total_score} |'
            # イニングごとの後攻チーム得点を追加
            else:
                score = inning_scores[Game.TURN['bot']] 
                if inning == Game.INNINGS - 1:  # 最終回の処理
                    if attack_first.total_score < defense_first.total_score:  # 9回の裏はやらない
                        score_boards[row] += ' X |'
                    else:
                        score_boards[row] += f' {score} |'
                        defense_first.total_score += score
                    score_boards[row] += f' {defense_first.total_score} |'
                else:
                    score_boards[row] += f' {score} |'
                    defense_first.total_score += score
    
    with open(Game.OUTPUT_LIST_PATH, 'a', encoding='utf-8') as f: 
        # スコアボードの描画
        border()
        for row in score_boards:
            print(row)
            f.write(row + '\n')
        border()

        # 勝敗判定
        winner: str = ''
        if attack_first.total_score == defense_first.total_score:
            print('引き分け')
        else:
            if attack_first.total_score > defense_first.total_score:
                winner = Game.PLAYERS[0]
            else:
                winner = Game.PLAYERS[1]
            print(winner + 'の勝ち')
        border()


if __name__ == '__main__':
    main()
