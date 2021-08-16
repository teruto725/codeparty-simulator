# coding: UTF-8
from importlib import import_module
import json
from game_controller2 import GameController

player_paths= ["players.sample2","players.sample2","players.sample2","players.sample2"]
player_num = 4
gamename = "square_paint"

if __name__ == '__main__':
    players = [import_module(path) for path in player_paths ]
    
    g_con = GameController(players, gamename)
    log = g_con.start()
    with open('./log/input.json', 'w') as f:
        json.dump(log, f, indent=4)
