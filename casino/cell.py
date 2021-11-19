class Cell:
    NAMES: list = ['R', 'B'] + [f'{num}' for num in range(1, 9)]
    RATES: list = [8, 2]
    COLORS: list = ['red', 'black', 'green']
    table: list = []
    
    def __init__(self, name: str, rate: int, color: str):
        self.name = name
        self.rate = rate
        self.color = color


class Color:
    BLACK: str = '\033[30m'
    RED: str = '\x1b[31m'
    GREEN: str = '\x1b[32m'
    END: str = '\x1b[0m'


def create_table():
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


def show_table():
    border: str = coloring(Cell.COLORS[2], '|')
    for cell in Cell.table:
        string: str = f' {cell.name}(x{cell.rate}) '
        colored_string: str = coloring(Cell.COLORS[0], string)
        print(border + colored_string + border)


def coloring(color: str, string: str):
    colored_string: str = ''
    if color == Cell.COLORS[0]:
        colored_string = Color.RED + string + Color.END
    elif color == Cell.COLORS[2]:
        colored_string = Color.GREEN + string + Color.END
    return colored_string
        
def main():
    # create_table()
    # show_table()
    print(Color.RED + 'test' + Color.END)


if __name__ == '__main__':
    main()