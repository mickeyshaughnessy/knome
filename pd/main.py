import numpy as np
from image.image import Drawer
from pd import Game, Player, SIZE, NSWAPS
import random


drawer = Drawer()

def swap(players, p1, p2, x1, y1, x2, y2):
    players[x1][y1] = p2
    players[x2][y2] = p1
    return players


if __name__ == "__main__":
    players = np.random.rand(SIZE, SIZE)
    players = [[Player(random.random()) for _ in range(SIZE)] for _ in range(SIZE)]
    
    game = Game()
    while True:
        print sum(map(sum, [[p.strat for p in _row] for _row in players]))/(SIZE**2)
        drawer.draw(np.array([[p.strat for p in _row] for _row in players]))
        for x in range(1,SIZE-1):
            for y in range(1,SIZE-1):
                player = players[x][y]
                move = player.play()
                opps = [(x+1,y+1), (x+1,y), (x+1,y-1), (x,y+1), (x,y), (x,y-1), (x-1,y+1), (x-1,y), (x-1,y-1)]
                opps = [players[_x][_y] for (_x,_y) in opps]
                moves = [opp.play() for opp in opps]
                results = [game.play(move, _move) for _move in moves]
                if sum(results) > 0:
                    player.add()
                else:
                    player.subtract()

        swaps = [(random.choice(range(SIZE)), random.choice(range(SIZE)), random.choice(range(SIZE)), random.choice(range(SIZE))) for _ in range(NSWAPS)]
        for _swap in swaps:
            p1 = players[_swap[0]][_swap[1]]
            p2 = players[_swap[2]][_swap[3]]
            players = swap(players, p1, p2, _swap[0], _swap[1], _swap[2], _swap[3])

    
