'''
Created on Sep 17, 2015

@author: H141517
'''
from Grid import Grid
from Player import Player

def main():
    '''
      Controller which starts the game.
    '''
    possible_color = ['red','blue','green','yellow','orange','brown','black']
    grid_size = 8
    players = []
    no_of_players = input("How many players")
    if no_of_players < 7 and no_of_players >1:
        count = 0
        while count < no_of_players:
            color = possible_color[count]
            name = 'Player_'+str(count)
            print 'color',color,'name',name
            players.append(Player(color,name))
            count += 1
        grid = Grid(grid_size,players)
        grid.play()
    else:
        print (" That no of players are not permitted")    
            
        
if __name__ == '__main__':
    main()