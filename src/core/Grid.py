'''
Created on Sep 17, 2015

@author: H141517
'''
from square import  Square
class Grid(object):
    '''
    classdocs
    '''
    def __init__(self, size,players):
        '''
        Constructor
        '''
        self.size = size
        self.players = players
        self.grid = [[]]
        self.winner = players[0]
        
    def play(self):
        
        count = -1
        self.create()
        is_completed = False
        no_of_players = len(self.players)
        while(not is_completed):
            count = (count + 1) % no_of_players
            self.players[count].started = True
            (x,y) = input('\n'+str(self.players[count].name)+'Enter the co-ordinates (x,y)'+'possible values [0..'+str(self.size-1)+'],[0..'+str(self.size-1)+']')
            effected = self.grid[x][y].on_click(self.players[count])
            while effected :
                if effected[0][0] != None and effected[0][1] != None:
                    temp = self.grid[effected[0][0]][effected[0][1]].on_click(self.players[count])
                del effected[0]
                if temp:
                    effected = effected + temp
                    temp = None
            self.display_grid()
            check_game_status = True;
            for player in self.players:
                check_game_status = check_game_status and player.started
            if check_game_status:
                is_completed = self.check_grid()
        print '\nWinner is ',self.winner.name  
         
    def create(self):
        for i in range(self.size):
            if i == len(self.grid):
                self.grid.append([])
            for j in range(self.size):
                self.grid[i].append(Square(i,j,self.size))      
                
    
    def display_grid(self):
        for i in range(self.size):
            print ''
            for j in range(self.size):
                if self.grid[i][j].belongs_to:
                     print self.grid[i][j].belongs_to.name,'=',self.grid[i][j].count,
                else:
                     print self.grid[i][j].belongs_to,'=',self.grid[i][j].count,
                     
    
    def check_grid(self):
        prev_player = None
        for i in range(self.size):
            for j in range(self.size):
                if not prev_player:
                    prev_player = self.grid[i][j].belongs_to
                else:
                    if self.grid[i][j].belongs_to != None and  prev_player != self.grid[i][j].belongs_to:
                        return False
        self.winner = prev_player
        return True
                        
                           
        
        
                
     
