import random

# T>R>P>S, 2R > T + S
P=0.0 # score when both defect
T=30.0 # score when I defect, you cooperate
S=-30.0 # score when I cooperate, you defect
R=25.0 # score when we both cooperate
SIZE = 100 
NSWAPS = 5 
DO_REP = False 

class Player():

    def __init__(self, strat):
        self.strat = strat # 0 is a pure defector, 1 is a pure cooperator
        self.total = 0
        self._id = hash(str(random.random()))

    def play(self, opp_rep=None):
        if opp_rep:
            # if the rep is high, they are likely to be a cooperator
            # if the rep is low, they are likely to be a defector
            if opp_rep > 0.5:
                return random.random()**2 < self.strat # more likely to cooperate
            else:
                return random.random() < self.strat**2 # more likely to defect
        else:
            return random.random() < self.strat # True is cooperate, False is defect 

    def add(self, num=0.03):
        if self.strat < 1.0:
            self.strat += num 
    
    def subtract(self, num=0.03):
        if self.strat > 0.0:
            self.strat -= num

    def rate(self, opp_moves):
        # rate opponents according to how much they defect
        return [float(m) for m in opp_moves]

class Game():

    def __init__(self, rep=None):
        self.reputation = rep
        self.matrix = {
                # T>R>P>S, 2R > T + S
                #(False, False) : 0.0, # both defect, P
                #(False, True) : 30.0, # I defect, you cooperate T
                #(True, False) : -30.0, # I cooperate, you defect S
                #(True, True) : 45.0 # we both cooperate, R
                (False, False) : P, # both defect, P
                (False, True) : T, # I defect, you cooperate T
                (True, False) : S, # I cooperate, you defect S
                (True, True) : R # we both cooperate, R
        }

    def play(self, move1, move2):
        return self.matrix[(move1, move2)]


