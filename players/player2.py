import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

import  random as rd

name = "RAMDOM MAN" 
def action(helper):
    return rd.randrange(4)