import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

import  random as rd

name = "ROUND SQUARE MAN" #名前を書く



def action(helper):
    my_point = helper.get_my_point(name)
    before_action_num = helper.get_before_action(name) #前回の行動
    around_tiles = helper.get_around_tiles(name) #周囲のマス配列

    if before_action_num == 4:
        before_action_num = 2

    if around_tiles[before_action_num].is_alive:
        

    if helper.get_up_tile().is_alive:
        return 0
    elif helper.get_down_tile().is_alive:
        return 1
    elif helper.get_left_tile().is_alive:
        return 2
    elif helper.get_right_tile().is_alive:
        return 3
    return 4
