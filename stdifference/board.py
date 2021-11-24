import random
import string
import numpy as np
from enum import Enum

KANJI: list = [('見', '貝'),
               ('土', '士'),
               ('眠', '眼'),
               ('犬', '尤')]
ALPHA: list = list(string.ascii_uppercase)
MIN_SIZE: int = 3


class Rarelity(Enum):
    COMMON = 0
    EPIC = 1


class Board:
    
    def __init__(self, row: int = MIN_SIZE, col: int = MIN_SIZE):
        self.row: int = row
        self.col: int = col
        self.kanji: tuple = ()
        self.table: np.ndarray = np.full((self.row, self.col), Rarelity.COMMON)
        self.set_kanji()
        self.set_epic()
        self.shuffle()

    def set_kanji(self):
        self.kanji = random.choice(KANJI)
    
    def set_epic(self):
        self.table[0, 0] = Rarelity.EPIC
        
    def get_epic(self):
        str_coord: str = ''
        row, col = list(zip(*np.where(self.table == Rarelity.EPIC)))[0]  # np.ndarrayの座標から整数を抽出
        str_coord = f'{ALPHA[col]}{row + 1}'
        return str_coord
    
    def shuffle(self):
        np.random.shuffle(self.table)
        for row in self.table:
            if Rarelity.EPIC in row:
                np.random.shuffle(row)
    
    def create_rows(self):
        rows: list = [horizontal_border(self.col),
                      get_second_row(self.col),
                      horizontal_border(self.col)]
        for row, cols in enumerate(self.table):
            rows.append(get_kanji_row(row + 1, cols, self.kanji))
        rows.append(horizontal_border(self.col))
        return rows

        
def horizontal_border(col: int):
    return '+----+-' + ('--' * col) + '-+'


def get_second_row(col: int):
    second_row: str = '|  / | '
    for index, chara in enumerate(ALPHA):
        if index < col:
            second_row += f' {chara}'
    return second_row + ' |'


def get_kanji_row(row: int, cols: list, kanji: tuple):
    kanji_row: str = f'| {row:>2} | '
    for chara in cols:
        if chara == Rarelity.COMMON:
            kanji_row += kanji[Rarelity.COMMON.value]
        else:
            kanji_row += kanji[Rarelity.EPIC.value]
    return kanji_row + ' |'
        

def main():
    bd = Board(6, 6)

    while True:
        print(bd.get_epic())
        for row in bd.create_rows():
            print(row)
        bd.set_kanji()
        bd.shuffle()
        input('press enter')
    

if __name__ == '__main__':
    main()
