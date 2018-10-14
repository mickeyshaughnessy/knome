import random

SIZE = 100 
NSWAPS = 10 

class Player():

    def __init__(self, strat):
        self.strat = strat # 0 is a pure defector, 1 is a pure cooperator

    def play(self):
        return random.random() < self.strat # True is cooperate, False is defect 

    def add(self, num=0.03):
        if self.strat < 1.0:
            self.strat += num 
    
    def subtract(self, num=0.03):
        if self.strat > 0.0:
            self.strat -= num 

class Game():

    def __init__(self):
        self.matrix = {
                # T>R>P>S, 2R > T + S
                (False, False) : -10, # both defect, P
                (False, True) : -9, # I defect, you cooperate T
                (True, False) : -10, # I cooperate, you defect S
                (True, True) : 29 # we both cooperate, R
        }

    def play(self, move1, move2):
        return self.matrix[(move1, move2)]

