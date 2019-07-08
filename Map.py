########################################################################
##
## CS 101
## Program #8
## Name: Harrison Lara
## Email: hrlwwd@mail.umkc.edu
##
## PROBLEM :
##   Write a puzzle game, called Wumpus World. Your program will provide the
##   user with feedback about what they can see; the user must use logic
##  (or guesswork, if they prefer) to try to succeed.
##
## ALGORITHM : 
## Main File: Program8.py
##    Handles all user interactions, gets input, checks it for validity,  passes valid input to methods of WumpusWorld object, provides user feedback based on results, computes final score.
##    Imported File 1: Map.py
##    class OffMapError, class Cell,  class Map should all be in source file Map.py 
##    class OffMapError(Exception):   raised if attempt to go off map.
##  Methods:
##     __init__(self) 
##    class Cell(object): Models one cell (square) in the map. 
##    Data:
##     self.hasWumpus  Boolean
##     self.hasGold Boolean
##     self.hasPit Boolean
##     self.hasBreeze  Boolean
##    self.hasStench  Boolean
##  Methods:
##     __init__(self)
##  class Map: manages the entire map, assigns values to cells, reports
##             status of map cells 
##  Data: 
##    self.grid  5x5 (0,0) – (4,4)
##  Methods: 
##    __init__(self)
##     onGrid(self, r, c)  Boolean
##    offGrid(self, r, c)  Boolean
##    reset(self)  User input
##    isBreezy(self, r, c)  Boolean
##    isSmelly(self, r, c)  Boolean
##    isGlinty(self, r, c)  Boolean
##     hasWumpus(self, r, c)  Boolean
##     hasPit(self, r, c)  Boolean
## Imported File 2: Wumpus.py
## Class WumpusWorld: contains a map, records player movement & current game state 
## Data:
##    self.worldmap
##    self.WumpusAlive  Boolean
##    self.playerAlive  Boolean
##    self.playerHasGold  Boolean
##    self.playerHasArrow  Boolean
##    self.playerMoves  Boolean
##    self.playerRow  (x axis)
##    self.playerCol (y axis)
##  Methods:
##     __init__(self)
##     Most of these use current player location 
##     stepEast(self)  User Input East
##     stepWest(self)  User Input West
##     stepSouth(self)  User Input South
##     stepNorth(self)  User Input North
##     
##    grab(self, r, c)  User Input Grab
##    grabGold(self)  User Input Grab Gold
##    checks current r, c, calls
##    fire(self, direction)  User Input Fire
##    canClimb(self)  User Input Climb
##    feelBreeze(self)   Boolean
##    smellStench(self) Boolean
##    seeGlint(self) Boolean
##    hasWumpus(self)  Boolean
##    hasPit(self) Boolean
##    5x5 grid, with cells numbered from 0,0 to 4,4.
##    The player starts at 0,0.
##    Players may take the following actions: 
##            North, South, East, West (Move one square in that direction)
##    5 pits, 1 Wumpus, 1 gold (all random placement, but stationary)
##    Pits > gold,
##    Wompus > gold (unless shot)
##    Wompus > pits
##    Climb out is at 0,0
##    Only the player can be placed at 0,0
##    Scoring: 
##    +1000 Climbed out with gold 
##    +100 Climbed out without gold 
##    -10 Fired weapon (only one arrow)
##    -1 per move
##    Score 0 if the player died
##    • Write a Cell class. This class will model one square in the map. A Cell simply has a few boolean variables; for example, hasPit, hasGold, isBreezy, etc.
##    • Write a Map class. A Map class contains a 2-dimensional list of Cells. It also has the following methods:
##          ◦ isBreezy(self, row, col): returns True if the specified cell is breezy, False otherwise.
##          ◦ isGlinty(self, row, col): returns True if the gold is in that square, false otherwise. 
##          ◦ hasWumpus(self, row, col): returns True if the Wumpus is there, false otherwise. 
##          ◦ hasPit(self, row, col): returns True if the cell has a pit, False otherwise
## Extra Notes:
##  bottom left corner will be 0,0, player spawns there to start
##  the grid will be 25 cells (5x5) or 0-4 on the x and y axis
##  Wumpus and gold spawns on one cell and doesn’t move
##  5 of the cells will be pits
##  Gold can be in a pit, never reachable gold
##  pit and Wumpus can be in the same cell but the Wumpus is greater than the pit
##  adjacent to Wumpus - smell stench
##  same cell as the gold - see a glint (grab gold)
##  user tries to go off grid- player feels a bump
##  player has one arrow to shoot and will go across all the cells in that direction
##  score is always zero if you die
##  minus score for shooting arrow and each move is a point deduction
##  use classes and functions given in the pdf
##  self.haswompus, etc should all be under the init(self) and Booleans
##  return true if on grid, off grid will return false
##  just write the code for each class under class given
##  no need to make any more classes
##  can use an int or a string with direction to go a certain way
##  should have 2 outsource files with the other classes
##  import the two other files
##  output that it is dark each time unless other
##  greet user and tell them their commands
##  climb out is at 0,0
##  import (name of file)
## 
## ERROR HANDLING:
##      
##
## OTHER COMMENTS:
##      None.
##
########################################################################

# Imports
import random

# Classes and Functions

class Map(object):
    ''' Map size and all the dangers for player and warnings signals'''
    
    def __init__(self, grid_size):
        ''' map area/size'''
        self.size = grid_size
        self.grid = []
        for row in range(0, self.size):
            row = []
            for col in range(0, self.size):
                row.append(Cell())
            self.grid.append(row)

    def reset(self):
        self = Map()
            
    def isBreezy(self, r, c):
        '''There is a pit near this cell'''
        return self.grid[r][c].isBreezy

    def isSmelly(self, r, c):
        '''There is a a wumpus near this cell'''
        return self.grid[r][c].isSmelly

    def isGlinty(self, r, c):
        '''There is gold near this cell'''
        return self.grid[r][c].isGlinty

    def hasWumpus(self, r, c):
        '''This cell has a wumpus'''
        return self.grid[r][c].hasWumpus
        
    def hasPit(self, r, c):
        '''This cell has a pit'''
        return self.grid[r][c].hasPit
        
    def __str__(self):
        s = ""
        for row in range(0, self.size):
            for col in range(0, self.size):
                s += "C "
            s += "\n"
        return s

class OffMapError(Exception):
    '''Returns the player to the map if they try and leave the grid'''
    def __init__(self):
            print('There seems to be a wall here')
            pass

class Cell(object):
    def __init__(self):
        self.hasWumpus = False
        self.hasGold = False
        self.hasPit = False
        self.hasBreeze = False
        self.hasStench = False
    
    
class __init__(object):
    '''Create wumpus, gold, pits, warning signals'''
    
    def __init__(self, wumpus_count):
        '''Create Wumpus'''
        count = 0
        # while loop continues until wumpus_count unoccupied positions are found
        while count < wumpus_count:
            x = random.randint(0,self.grid_size - 1)
            y = random.randint(0,self.grid_size - 1)
            if not self.wumpus(x,y):
                new_wumpus = wumpus(Map = self, x = x, y = y)
                count = 1             

        def register(self,user):
            '''Register item with map'''
            x = user.x
            y = user.y
            self.grid[x][y] = user

    def hasGold(self, gold_count):
        ''' Create Gold'''
        count = 0
        # while loop continues until gold_count unoccupied positions are found
        while count < gold_count:
            x = random.randint(0,self.grid_size - 1)
            y = random.randint(0,self.grid_size - 1)
            if not self.gold(x,y):
                new_gold = gold(Map = self, x = x, y = y)
                count = 1
                
        def remove(self, user):
            '''Remove user from cell.'''
            x = user.x
            y = user.y
            self.grid[x][y] = 0
                
    def hasPit(self, pit_count):
        ''' Create Pit'''
        count = 0
        # while loop continues until pit_count unoccupied positions are found
        while count < pit_count:
            x = random.randint(0,self.grid_size - 1)
            y = random.randint(0,self.grid_size - 1)
            if not self.pit(x,y):
                new_pit = pit(Map = self, x = x, y = y)
                count += 1
                self.register(new_pit)
        count = 5
       
    def hasBreeze(self):
        ''' Create breeze (pit near) warning'''
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)] 
        result = 0
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if not 0 <= x < self.Map.size() or \
               not 0 <= y < self.Map.size():
                continue
            if type(self.Map.user(x,y)) == type_looking_for:
                result =(x,y)
                break
        return result
        
    def hasStench(self):
        ''' Create stench (wumpus near) warning'''
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        result = 0
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if not 0 <= x < self.Map.size() or \
               not 0 <= y < self.Map.size():
                continue
            if type(self.Map.user(x,y)) == type_looking_for:
                result =(x,y)
                break
        return result
        
    def onGrid(self, r, c):
        ''' Makes sure the user and dangers are within the grid'''
       if r in range (0,4) and c in range (0,4):
           return True
        else:
            raise OffMapError
    






