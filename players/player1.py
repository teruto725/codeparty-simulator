import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

import  random as rd

name = "player1" #名前を書く
def action(helper):
    return rd.randrange(4)