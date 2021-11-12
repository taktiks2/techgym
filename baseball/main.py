import random
from operafile import open_csv

CSV_FILE: str = 'input/teamlist.csv'


class Team():
    def __init__(self, id_num: int, name: str, attack: int, defense: int):
        self.id_num: int = id_num
        self.name: str = name
        self.attack: int = attack
        self.defense: int = defense
        self.total_score: int = 0
    
    def info(self):
        print(f'{self.id_num} ) {self.name}: 攻撃力:{self.attack} / 守備力:{self.defense}')
    
    def get_hit_rate(self):
        hit_rate: int = random.randint(10, self.attack)
        return hit_rate
    
    def get_out_rate(self):
        out_rate: int = random.randint(10, self.defense)
        return out_rate    
    

def create_teams():
    '''Teamインスタンスのリストを作成
    teamlist.csv内の各行にある情報から各チームのインスタンスを作成する
    id_num,name,attack,defense
    
    return: list
    '''
    teams: list = []
    team_info: dict = open_csv(CSV_FILE)
    for status in team_info.values():
        id_num: int = int(status[0])
        name: str = status[1]
        attack: int = int(status[2])
        defense: int = int(status[3])
        teams.append(Team(id_num, name, attack, defense))
        
    return teams


def get_inning_scores(playing_teams: dict):
    '''ゲームに使うチーム情報から得点を計算
    return: dict
    '''
    score: int = 0
    inning_scores: dict = {'top': 0,
                           'bottom': 0}
    team_keys: list = list(playing_teams.keys())
    print(f'デバッグ: {team_keys}')
    
    # 1イニング分のスコアを計算
    for turn in inning_scores:
        # 裏になったらリストを反転させて攻守交替
        if turn == 'bottom':
            team_keys.reverse()
        attack: Team = playing_teams[team_keys[0]]
        defense: Team = playing_teams[team_keys[1]]
    
        score = (attack.get_hit_rate() - defense.get_out_rate()) // 10
        
        if score < 0:
            score = 0
        inning_scores[turn] = score
    
    return inning_scores



def border():
    print('----------------------------------------------------------')


def main():
    teams: list = create_teams()
    player_names: list = ['自分', '相手']
    playing_teams: dict = {}
    len_game: int = 9
    score_table: dict = {}
    
    # チーム情報を表示する
    border()
    print('全チーム情報')
    border()
    for team in teams:
        team.info()
    border()

    # チーム選択
    for player in player_names:
        id_num: int = int(input(f'{player}のチームを選択してください(1~{len(teams)})')) - 1
        playing_teams[player] = teams[id_num]
        print(f'{player}は「{playing_teams[player].name}」を選択しました')
    
    # len_gameの回数だけイニングを繰り返す
    for number in range(len_game):
        inning_scores: dict = get_inning_scores(playing_teams)
        score_table[number] = inning_scores
        
    score_boards: list = ['____|',
                         f'{player_names[0]}|',
                         f'{player_names[1]}|']
    attack: Team = playing_teams[player_names[0]]
    defense: Team = playing_teams[player_names[1]]
    
    # 各チームの総得点計算
    for score in score_table.values():
        attack.total_score += score['top']
        defense.total_score += score['bottom']
    
    # 回と合計のカラム作成
    for num_inning in range(1, len_game + 1):
        score_boards[0] += f' {num_inning} |'
        if num_inning == 9:
            score_boards[0] += ' R |'
    # 回ごとのattackチーム得点を追加
    for num_inning in range(len_game):
        score_boards[1] += f' {score_table[num_inning]["top"]} |'
        if num_inning == 8:
            score_boards[1] += f' {attack.total_score} |'
    for num_inning in range(len_game):
        score_boards[2] += f' {score_table[num_inning]["bottom"]} |'
        if num_inning == 8:
            score_boards[2] += f' {defense.total_score} |'

    for row in score_boards:
        print(row)    

if __name__ == '__main__':
    main()