
    
class Game():
    start_point = [[2,2,0],[2,9,0],[9,2,0],[9,9,0]]
    def __init__(self,names):
        self.p_num = 4
        self.max_x = 10
        self.max_y = 10
        self.max_z = 5
        self.players = [Player(name,Game.start_point[i]) for i,name in enumerate(names)]
        self.tiles = Tiles(self.max_x,self.max_y,self.max_z)
        self.turn_num = 0
        self.helper = Helper(self.tiles,self.players)

        #初期位置のちぇっく
        for player in self.players:
            self.tiles.check_player_move(player)



    def get_helper(self):
        return self.helper

    #actionを受け取る
    def do_action(self,p_num,action):
        player = self.players[p_num]
        player.move(action)#移動する
        self.tiles.check_player_move(player)# 移動したときどうなるか
    
    #tileを更新する
    def next_turn(self):
        self.turn_num += 1
        self.tiles.update()

    #一人だけ生きてたらtrue
    def is_end(self):
        count = 0
        for player in self.players:
            if player.is_alive:
                count += 1
        return count <= 1

    # logを返す
    def get_log(self):
        log = {
            "turn_num":self.turn_num,
            "tiles": self.tiles.to_log(),
            "players": [player.to_log() for player in self.players] 
        }
        return log

    #最終結果のlog
    def get_result_log(self):
        for player in self.players:
            if player.is_alive:
                return player
        

class Tiles():
    def __init__(self,x_max,y_max,z_max):
        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max
        self.tiles = []
        for x in range(x_max+2):
            y_li = []
            for y in range(y_max+2):
                x_li = []
                for z in range(z_max+1):
                    x_li.append(Tile())
                y_li.append(x_li)
            self.tiles.append(y_li)
        self._create_dead_area()#周りのマスを空にしておく
        self.pressed_tiles = []#更新が必要なタイルたち
    
    #周りに空のエリアを作る
    def _create_dead_area(self): 
        for x in range(self.x_max+2):
            for y in range(self.y_max+2):
                for z in range(self.z_max+1):
                    if x == 0 or x == self.x_max+1 or y == 0 or y == self.y_max+1 or z == self.z_max:
                        self.tiles[x][y][z].is_alive = False

    #タイルを更新する 死んだらpressedtileから削除しておく
    def update(self):
        for i in reversed(range(len(self.pressed_tiles))):
            self.pressed_tiles[i].update()
            if self.pressed_tiles[i].is_alive == False:
                self.pressed_tiles.pop(i)

    #行動に応じてplayerを行動させる
    def check_player_move(self,player):
        point = player.get_point()
        tile = self.tiles[point[0]][point[1]][point[2]]
        if point[2] == self.z_max: #最下層なら問答無用で殺す
            player.is_alive = False
        else:
            if tile.is_alive: # タイルがあればfalling = Falseなければfalling
                player.is_falling = False
                tile.is_pressed = True#タイルを踏んだのでtrueにする
                self.pressed_tiles.append(tile)
            else:
                player.is_falling = True

    # 配列にする
    def to_log(self):
        tiles_arr = []
        for x in range(self.x_max+2):
            li_y = []
            for y in range(self.y_max+2):
                li_z = []
                for z in range(self.z_max+1):
                    li_z.append(self.tiles[x][y][z].is_alive)
                li_y.append(li_z)
            tiles_arr.append(li_y)
        return tiles_arr


class Tile():
    dead_count = 1 # タイルが消えるまでの時間
    def __init__(self):
        self.is_alive = True
        self.is_pressed = False
        self.count = Tile.dead_count
        
    #countを小さくする　0になったら消える
    def update(self):
        self.count = self.count -1
        if self.count == 0:
            self.is_alive = False
    

class Player():
    def __init__(self,name,start_point):
        self.name = name
        self.point = start_point
        self.is_alive = True # 生きているか
        self.is_falling = False # 落ちているか

    #移動する
    def move(self,action):
        if self.is_alive:
            if self.is_falling:#落ちている状況なら落ちる
                self.point = [self.point[0], self.point[1], self.point[2]+1]
            elif action == 0:
                self.point =  [self.point[0], self.point[1]-1, self.point[2]]
            elif action == 1:
                self.point =  [self.point[0], self.point[1]+1, self.point[2]]
            elif action == 2:
                self.point =  [self.point[0]-1, self.point[1], self.point[2]]
            elif action == 3:
                self.point =  [self.point[0]+1, self.point[1], self.point[2]]
            elif action == 4:
                self.point =  [self.point[0], self.point[1], self.point[2]]
            else:
                print("Action Error")
    
    def to_log(self):
        return {
            "name": self.name,
            "point": self.point,
            "is_alive": self.is_alive,
            "is_falling": self.is_falling
        }

    def get_point(self):
        return self.point

class Helper():
    def __init__(self,tiles,players):
        self.tiles = tiles
        self.players = players

    def labeling(self,level):
        #level層目をラベリングしてラベリング結果の２次元配列を返す
        x_max = self.tiles.x_max+2
        y_max = self.tiles.y_max+2

        labeled = [[(i*x_max+j if self.tiles.tiles[i][j][level].is_alive else -1)for j in range(y_max)] for i in range(x_max)]
        changed = True
        while changed:
            changed= False
            for i in range(x_max):
                for j in range(y_max):
                    candidate = []
                    if(labeled[i][j] == -1):
                        continue
                    if(i>=1 and self.tiles.tiles[i-1][j][level].is_alive):
                        candidate+=[labeled[i-1][j]]
                    if(j>=1 and self.tiles.tiles[i][j-1][level].is_alive):
                        candidate+=[labeled[i][j-1]]
                    if(i<=self.tiles.y_max-2 and self.tiles.tiles[i+1][j][level].is_alive):
                        candidate+=[labeled[i+1][j]]
                    if(j<=self.tiles.x_max-2 and self.tiles.tiles[i][j][level].is_alive):
                        candidate+=[labeled[i][j+1]]
                    mini = min(candidate)
                    if(mini < labeled[i][j]):
                        changed = True
                        labeled[i][j] = mini
        return labeled
