import numpy as np
from image.image import Drawer
from pd import Game, Player, SIZE, NSWAPS, DO_REP
from reputation import Reputation
import random


drawer = Drawer(magnify=3)
rep = Reputation(DO_REP)

def swap(players, p1, p2, x1, y1, x2, y2):
    players[x1][y1] = p2
    players[x2][y2] = p1
    return players


if __name__ == "__main__":
    players = np.random.rand(SIZE, SIZE)
    players = [[Player(random.random()) for _ in range(SIZE)] for _ in range(SIZE)]
    
    game = Game(rep=rep)
    N = 0
    while True:
        ### Reporting and drawing ###
        N += 1
        # reports iteration number and average strategy (degree of cooperation)
        print N, sum(map(sum, [[p.strat for p in _row] for _row in players]))/(SIZE**2)
        drawer.draw(np.array([[p.strat for p in _row] for _row in players]), "strategies")
        drawer.draw(np.array([[p.total for p in _row] for _row in players]), "totals", norm=True)
        if DO_REP:
            drawer.draw(np.array([[game.reputation.get_rep(p._id) for p in _row] for _row in players]), "reputations")
       
        ### main loop ###
        for x in range(1,SIZE-1):
            for y in range(1,SIZE-1):
                player = players[x][y]
                opps = [(x+1,y+1), (x+1,y), (x+1,y-1), (x,y+1), (x,y), (x,y-1), (x-1,y+1), (x-1,y), (x-1,y-1)]
                opps = [players[_x][_y] for (_x,_y) in opps]
                opp_moves = [opp.play(game.reputation.get_rep(player._id)) for opp in opps]
                my_moves = [player.play(game.reputation.get_rep(opp._id)) for opp in opps]
                results = [game.play(my_move, _move) for (my_move, _move) in zip(my_moves, opp_moves)]
                player.total += sum(results)

                if DO_REP:
                    reviews = player.rate(opp_moves)
                    game.reputation.review(player, opps, reviews)

                if random.random() < 0.1:
                    # check another nearby player's strategy. If it is better, adopt it.
                    other = random.choice(opps)
                    if other.total > player.total:
                        player.strat = other.strat

        swaps = [(random.choice(range(SIZE)), random.choice(range(SIZE)), random.choice(range(SIZE)), random.choice(range(SIZE))) for _ in range(NSWAPS)]
        for _swap in swaps:
            p1 = players[_swap[0]][_swap[1]]
            p2 = players[_swap[2]][_swap[3]]
            players = swap(players, p1, p2, _swap[0], _swap[1], _swap[2], _swap[3])

    
