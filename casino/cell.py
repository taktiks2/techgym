class Cell:
    NAMES: list = ['R', 'B'] + [f'{num}' for num in range(1, 9)]
    RATES: list = [8, 2]
    COLORS: list = ['red', 'black']
    table: list = []
    
    def __init__(self, name: str, rate: int, color: str):
        self.name = name
        self.rate = rate
        self.color = color

def create_table():
    pass

def show_table():
    pass


def main():
    table: list = []
    print(Cell.NAMES)

    
if __name__ == '__main__':
    main()