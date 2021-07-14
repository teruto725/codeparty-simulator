import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

import  random as rd

name = "AVOID HOLE MAN" #名前を書く



def action(helper):
    if helper.get_up_tile(name).is_alive:
        return 0
    elif helper.get_down_tile(name).is_alive:
        return 1
    elif helper.get_left_tile(name).is_alive:
        return 2
    elif helper.get_right_tile(name).is_alive:
        return 3
    return 4
