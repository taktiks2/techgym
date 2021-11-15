import random
from operafile import open_csv

CSV_FILE: str = 'input/teamlist.csv'


class Game():
    LENGTH: int = 9
    PLAYERS: list = ['自分', '相手']


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
    return例: [Team(3, '中日ドラゴンズ', 50, 50), Team(2, '阪神タイガース', 30, 70)]
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
    return例: {'top': 3, 'bottom': 2}
    '''
    score: int = 0
    inning_scores: dict = {'top': 0,
                           'bottom': 0}
    team_keys: list = list(playing_teams.keys())
    
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
    playing_teams: dict = {}
    
    # チーム情報を表示する
    border()
    print('全チーム情報')
    border()
    for team in teams:
        team.info()
    border()

    # チーム選択
    for player in Game.PLAYERS:
        id_num: int = int(input(f'{player}のチームを選択してください(1~{len(teams)}): ')) - 1
        playing_teams[player] = teams[id_num]
        if player == Game.PLAYERS[0]:
            attack: Team = playing_teams[player]
            name = attack.name
        else:
            defense: Team = playing_teams[player]
            name = defense.name
        print(f'{player}は「{name}」を選択しました')
        border()
    
    # スコアボードの描画
    score_boards: list = ['____|',
                         f'{Game.PLAYERS[0]}|',
                         f'{Game.PLAYERS[1]}|']
    for num_inning in range(Game.LENGTH):
        inning_scores: dict = get_inning_scores(playing_teams)
        for index in range(len(score_boards)):
            # 回と合計のカラム作成
            if index == 0:
                score_boards[index] += f' {num_inning + 1} |'
                if num_inning == Game.LENGTH - 1:  # 最終回の処理
                    score_boards[index] += ' R |'
            # 回ごとのattackチーム得点を追加
            elif index == 1:
                score = inning_scores['top']
                score_boards[index] += f' {score} |'
                print(f'{num_inning + 1}回表: {score}点')  # デバッグ用
                attack.total_score += score
                if num_inning == Game.LENGTH - 1:
                    score_boards[index] += f' {attack.total_score} |'
            # 回ごとのdeffenseチーム得点を追加
            else:
                score = inning_scores['bottom']
                if num_inning == Game.LENGTH - 1:
                    if attack.total_score < defense.total_score:
                        score_boards[index] += ' X |' 
                    else:
                        score_boards[index] += f' {score} |'
                        print(f'{num_inning + 1}回裏: {score}点')  # デバッグ用
                        defense.total_score += score
                    score_boards[index] += f' {defense.total_score} |'
                else:
                    score_boards[index] += f' {score} |'
                    print(f'{num_inning + 1}回裏: {score}点')  # デバッグ用
                    defense.total_score += score
                

    border()
    for row in score_boards:
        print(row)
    border()


if __name__ == '__main__':
    main()