import sys
sys.path.append('../')
from games.square_paint import Helper,Player,Tile,Tiles

import  random as rd

name = "Sample2" #名前を書く
def action(helper):
    stack = [0,1,2,3]
    return stack[rd.randrange(len(stack))]