import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

name = "SUGI" #名前を書く
c_dir = 0
#踏まれているもしくはタイルが無い地点にたどり着いた場合，左に曲がるAI
def action(helper):
    global c_dir
    tiles = [helper.get_up_tile(name), helper.get_left_tile(name), helper.get_down_tile(name), helper.get_right_tile(name)]
    for i in range(4):
        idx = (c_dir + i) % 4
        if not tiles[idx].is_pressed and tiles[idx].is_alive:
            c_dir = idx
            break
    return c_dir
