class Status:
    MAX_LIFE: int = 3


class Player:
    
    def __init__(self, name: str):
        self.name: str = name
        self.life: int = Status.MAX_LIFE
        self.hand = None
    
        
class Computer(Player):
    
    def __init__(self, name: str):
        super().__init__(name)
    

def main():
    pass


if __name__ == "__main__":
    main()