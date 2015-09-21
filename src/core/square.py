'''
Created on Sep 17, 2015

@author: H141517
'''
class Square(object):
    '''
    This class is used to create square in the grid.
    '''


    def __init__(self,x,y,grid_size):
        '''
        Create a square object which has the following properties
        1) x,y : Co-ordinate for the square
        2) limit : Limit of the square how much it can hold
        3) next: If the block is clicked how the spheres propogate
        4) belongs_to : To which player this square block belongs .It holds the object of the Player class
        5) count : no. of sphere that is present in the square
        '''
        self.x = x
        self.y = y
        if (x == 0 and y == 0) or (x == 0 and y == (grid_size-1)) or (x == (grid_size-1) and y == 0) or (x == (grid_size-1) and y == (grid_size-1)):
            self.limit = 1
        elif x == 0 or y == 0 or x ==  (grid_size-1) or y ==  (grid_size-1):
            self.limit = 2
        else :
            self.limit = 3
        
        self.next = [(x+1 if x < grid_size-1 else None,y),(x,y+1 if y < grid_size-1 else None),(x-1 if x > 0 else None,y),(x,y-1 if y>0 else None)]
        self.belongs_to = None
        self.count = 0
        
    def on_click(self,clickedBy):
        '''
        Response method when the particular square is clicked by the player or 
        square is approached by the sphere that is right next
        '''
        if not self.belongs_to:
            self.count += 1
            self.belongs_to = clickedBy
        else:
            if self.count == self.limit:
                self.belongs_to = None
                self.count = 0
                return self.next
            else:
                self.count += 1
                if self.belongs_to != clickedBy:
                    self.belongs_to = clickedBy 
                
        return None
    
    
        
          
        
        