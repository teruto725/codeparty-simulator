import sys
sys.path.append('../')
from square_drop import Helper,Player,Tile,Tiles

name = "JUST MOVING MAN" #名前を書く
c_dir = 0
#踏まれているもしくはタイルが無い地点にたどり着いた場合，左に曲がるAI
def action(helper):
    tiles = [helper.get_up_tile(), helper.get_left_tile(), helper.get_down_tile(), helper.get_right_tile()]
    for i in range(4):
        idx = (c_dir + i) % 4
        if not tiles[idx].is_pressed and tiles[idx].is_alive:
            c_dir = idx
            break
    return c_dir
