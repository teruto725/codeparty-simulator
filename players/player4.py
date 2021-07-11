import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

import  random as rd

name = "player4"
def action(helper):
    return rd.randrange(4)
    