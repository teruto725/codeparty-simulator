# coding: UTF-8
from importlib import import_module
import json
from game_controller import GameController

player_paths= ["players.player1","players.player2","players.player3","players.player5"]
player_num = 4


if __name__ == '__main__':
    players = [import_module(path) for path in player_paths ]
    
    g_con = GameController(players)
    log = g_con.start()
    with open('./log/input.json', 'w') as f:
        json.dump({"game_info":log}, f, indent=4)
