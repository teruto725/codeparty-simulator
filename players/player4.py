import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

import  random as rd

name = "AVOID HOLE MAN" #名前を書く
def action(helper):
    stack = []
    if helper.get_up_tile().is_alive :
        stack.append(0)
    elif helper.get_down_tile().is_alive:
        stack.append(1)
    elif helper.get_left_tile().is_alive:
        stack.append(2)
    elif helper.get_right_tile().is_alive:
        stack.append(3)
    if stack == 
    rd.randrange(len(stack))
    return 4
