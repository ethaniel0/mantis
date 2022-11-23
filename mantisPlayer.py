class MantisPlayer:
    def __init__(self, name, number):
        self.draw = []
        self.mantis = False
        self.mantisCount = 0
        self.mantisCard = None
        self.mantisCardCount = 0
    
    def play(self, topcard, turn, hands, collecteds) -> int:
        pass