import random

class Reputation():

    def __init__(self, active):
        self.ledger = {} 
        self.active=active

    def review(self, player, opps, reviews):
        for opp, r in zip(opps, reviews):
            rep = self.ledger.get(opp._id, 0.5)
            
            if r > 0.5: # if good review, increase a bit
                d = (1.0 - rep)
                dr = d * r / 2.0 
                rep += dr
                self.ledger[opp._id] = min(1.0, rep)
            else: # if bad review, decrease a bit
                d = rep
                dr = d * (1.0 - r) / 2.0
                rep -= dr
                self.ledger[opp._id] = max(0, rep)

    def get_rep(self, _id=None):
        # higher reputation is better
        # max reputation is 1.0, min is 0.0
        if self.active:
            return self.ledger.get(_id, 0.5) 
        else:
            return None
