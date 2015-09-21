'''
Created on Sep 17, 2015

@author: H141517
'''

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, color,name):
        '''
        Constructor
        '''
        self.color = color
        self.name = name
        self.started = False