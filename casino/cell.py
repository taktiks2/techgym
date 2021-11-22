class Cell:
    NAMES: list = ['R', 'B'] + [f'{num}' for num in range(1, 9)]
    RATES: list = [8, 2]
    COLORS: list = ['red', 'black', 'green', 'yellow']
    table: list = []
    
    def __init__(self, name: str, rate: int, color: str):
        self.name: str = name
        self.rate: int = rate
        self.color: str = color


class Color:
    BLACK: str = '\033[30m'
    RED: str = '\033[31m'
    GREEN: str = '\033[32m'
    YELLOW: str = '\033[33m'
    END: str = '\033[0m'


def create_table():
    Cell.table = []
    for index in range(len(Cell.NAMES)):
        name: str = Cell.NAMES[index]
        rate: int = 0
        color: str = ''                                     
        if index == 0 or index == 1:
            rate = Cell.RATES[0]
        else:
            rate = Cell.RATES[1]    
        if index % 2 == 0:
            color = Cell.COLORS[0]
        else:
            color = Cell.COLORS[1]
        Cell.table.append(Cell(name, rate, color)) 


def coloring(color: str, string: str):
    colored_string: str = ''
    if color == Cell.COLORS[0]:
        colored_string = Color.RED + string + Color.END
    elif color == Cell.COLORS[2]:
        colored_string = Color.GREEN + string + Color.END
    elif color == Cell.COLORS[3]:
        colored_string = Color.YELLOW + string + Color.END
    return colored_string

        
def main():
    string = coloring()


if __name__ == '__main__':
    main()
