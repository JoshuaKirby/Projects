'''
Created on Feb 24, 2016

@author: jokirby
'''
import Display 
import Controls
import Turn

class Application():

    def __init__(self):
        display = Display()
        controls = Controls()
        turn = Turn()
        turn.takeTurn(controls)
        pass
    
    def turn(self):
        pass

if __name__ == '__main__':
    pass