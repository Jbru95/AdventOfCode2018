'''
Day 15 - Goblins vs. Elves
'''
import copy
class BattleGrid:
    
    def __init__(self):
        self.turns = 0
        self.unitReadingOrderArray = []
        self.goblinUnitArray = []
        self.elfUnitArray = []
        self.unitDict = {}
        self.grid = []
        fp = open('test_input.txt','r')
        for line in fp.readlines():
            self.maxj = len(line.strip())
            temp_row = []
            for char in line.strip():
                temp_row.append(char)
            self.grid.append(temp_row)
        fp.close()
        self.maxi = len(self.grid)

        self.initializeUnits()

    def __str__(self):
        ret_str = " Turn: " + str(self.turns) + '\n'
        for row in self.grid:
            for elem in row:
                ret_str += str(elem)
            ret_str += '\n'
        
        for unit in self.unitReadingOrderArray:
            ret_str += str(unit)
            ret_str += '\n'
        return ret_str

    def initializeUnits(self):
        for i  in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'E':
                    unit = Unit('E',i,j)
                    self.unitReadingOrderArray.append(unit)
                    self.elfUnitArray.append(unit)
                    self.unitDict[str(i)+','+str(j)] = unit
                elif self.grid[i][j] == 'G':
                    unit = Unit('G',i,j)
                    self.goblinUnitArray.append(unit)
                    self.unitReadingOrderArray.append(unit)
                    self.unitDict[str(i)+','+str(j)] = unit

    def updateUnitReadingOrderArray(self):
        self.unitReadingOrderArray = []
        for i  in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] =="E" or self.grid[i][j] =="G":
                    self.unitReadingOrderArray.append(self.unitDict[str(i)+','+str(j)])

    def performUnitActions(self):
        self.updateUnitReadingOrderArray()

        for unit in self.unitReadingOrderArray:
            unit.performAction(self)
        self.turns += 1
        self.updateUnitReadingOrderArray()

    


class Unit:

    def __init__(self, Type, i, j):
        self.i = i
        self.j = j
        self.hp = 200
        self.dmg = 3
        self.type = Type
        if self.type == "E":
            self.enemyType = "G"
        elif self.type == "G":
            self.enemyType = "E"

    def __str__(self):
        ret_str = ""
        ret_str += str(self.type) + " at " + str(self.i) + "," + str(self.j) + "   HP=" + str(self.hp) + ", DMG=" + str(self.dmg) + ':'
        return ret_str

    def __repr__(self):
        ret_str = ""
        ret_str += str(self.type) + " at " + str(self.i) + "," + str(self.j) + "   HP=" + str(self.hp) + ", DMG=" + str(self.dmg) + ';'
        return ret_str

    def returnOpenAdjacentSpaces(self, copyGrid, i, j): #returns an Array of Tuple (i,j) with the position of open Adjacent Spaces to the unit this is called on
        openSpaceTupArray = []
        if copyGrid[i - 1][j] == '.':
            openSpaceTupArray.append((i - 1,j))
        if copyGrid[i][j-1] == '.':
            openSpaceTupArray.append((i,j-1))
        if copyGrid[i][j+1] == '.':
            openSpaceTupArray.append((i,j+1))
        if copyGrid[i + 1][j] == '.':
            openSpaceTupArray.append((i+1,j))
        return openSpaceTupArray

    def inRangeOfEnemy(self, game): #if in range of an enemy unit returns the space of the first in reading order, otherwise returns None
        enemyUnitsInRangeArray = []
        if game.grid[self.i - 1][self.j] == self.enemyType:
            enemyUnitsInRangeArray.append((self.i - 1,self.j))
        if game.grid[self.i][self.j-1] == self.enemyType:
            enemyUnitsInRangeArray.append((self.i,self.j-1))
        if game.grid[self.i][self.j+1] == self.enemyType:
            enemyUnitsInRangeArray.append((self.i,self.j+1))
        if game.grid[self.i + 1][self.j] == self.enemyType:
            enemyUnitsInRangeArray.append((self.i+1,self.j))

        if len(enemyUnitsInRangeArray) == 0:
            return None
        else:
            lowest_hp = 1000
            for tup in enemyUnitsInRangeArray:
                if game.unitDict[str(tup[0]) + ',' + str(tup[1])].hp < lowest_hp:
                    lowest_hp = game.unitDict[str(tup[0]) + ',' + str(tup[1])].hp
            
            for tup in enemyUnitsInRangeArray:
                if game.unitDict[str(tup[0]) + ',' + str(tup[1])].hp == lowest_hp:
                    return tup #another  heuristic because the array is already in reading order, selecting the first one with lowest hp, will select earliest in reading order if there is a tie




    def attack(self, game, positionToAttackTup):
        enemyUnit = game.unitDict[str(positionToAttackTup[0]) + ',' + str(positionToAttackTup[1])]
        enemyUnit.hp -= self.dmg #reduce the health of the enemy at the attaack position by the units damage value
        if enemyUnit.hp <= 0:

            game.unitReadingOrderArray.remove(enemyUnit)
            if enemyUnit.type == "G":
                game.goblinUnitArray.remove(enemyUnit)
            if enemyUnit.type =="E":
                game.elfUnitArray.remove(enemyUnit)
            game.grid[enemyUnit.i][enemyUnit.j] = '.'
            del game.unitDict[str(positionToAttackTup[0]) + ',' + str(positionToAttackTup[1])]

    #def stepDistance(self, )
    def move(self, game, moveTup):
        if moveTup != None:
            del game.unitDict[str(self.i) + ',' + str(self.j)]
            game.grid[self.i][self.j] = '.'
            self.i = moveTup[0]
            self.j = moveTup[1]
            game.unitDict[str(self.i) + ',' + str(self.j)] = self
            game.grid[self.i][self.j] = self.type

    def performAction(self, game):
        enemyOpenSpaces = []
        if self.type == 'G':
            for unit in game.elfUnitArray:
                enemyOpenSpaces.extend(unit.returnOpenAdjacentSpaces(copy.deepcopy(game.grid), unit.i, unit.j)) #adding to array of open Enemy Spaces (possible movement targets)
        elif self.type == 'E':
            for unit in game.goblinUnitArray:
                enemyOpenSpaces.extend(unit.returnOpenAdjacentSpaces(copy.deepcopy(game.grid), unit.i, unit.j)) #adding to array of open Enemy Spaces (possible movement targets)
        #print(enemyOpenSpaces, self.inRangeOfEnemy(game))
        if (len(enemyOpenSpaces) == 0) and (self.inRangeOfEnemy(game) == None): #checking to see if any moves are possible
            return None
        
        if(self.inRangeOfEnemy(game) != None): #in range of enemy so attack
            self.attack(game, self.inRangeOfEnemy(game))
    
        else: #enemy has open spaces and there is not an enemy in range so time to move
            moveSpace = self.returnMoveSpace(copy.deepcopy(game.grid), game.goblinUnitArray.copy(), game.elfUnitArray.copy())
            self.move(game, moveSpace)
            if(self.inRangeOfEnemy(game) != None): #in range of enemy so attack
                self.attack(game, self.inRangeOfEnemy(game))


    def returnMoveSpace(self, grid, goblinArray, elfArray): #return a space to move to, or return None if the unit shouldn't move
        #print('in return move space')
        gridCopy = copy.deepcopy(grid) # DeepCopy the grid so we can manipulate the spaces without changing the original
        spaceOptionsArray = [] # Array containing (i,j) tups of all the open adjacent spaces a unit can move to 
        possibleDestinations = [] # Array containing (i,j) tups of all the possible dedtination spaces for this unit

        spaceOptionsArray.extend(self.returnOpenAdjacentSpaces(gridCopy, self.i, self.j)) #fill spaceOptionsArray 

        if self.type == "E": # if the unit were moving is an elf, fill destinations withs open adjacent squares from a G
            for unit in goblinArray:
                possibleDestinations.extend(self.returnOpenAdjacentSpaces(gridCopy, unit.i, unit.j))

        if self.type == "G": # do the opposite if the unit moving is a goblin
            for unit in elfArray:
                possibleDestinations.extend(self.returnOpenAdjacentSpaces(gridCopy, unit.i, unit.j))

        #print(spaceOptionsArray, possibleDestinations)

        origTempSpaceArray = copy.deepcopy(spaceOptionsArray) #deepCopy SpaceOptionArray
        nextTempSpaceArray = [] #Array containing the next loop of Spaces to Evaluate

        for i in range(1,20): #evaluates spaces around the unit, and then around those spaces, in order to calculate distances to all reachable points from the unit
            for tup in origTempSpaceArray: #evaluate positions in Array holding the temporary spaces to evaluate
                gridCopy[tup[0]][tup[1]] = i #set those positions on the map to the current distance (i)
                nextTempSpaceArray.extend(self.returnOpenAdjacentSpaces(gridCopy, tup[0], tup[1])) #Add newly found spaces for the next iteration in this array

            origTempSpaceArray = nextTempSpaceArray.copy() #swap the next array with the current one
            nextTempSpaceArray = [] #empty the next array so it can be refilled

        lowestNum = 1000
        for spaceTup in possibleDestinations:  #for all possible destination spaces
            space = gridCopy[spaceTup[0]][spaceTup[1]] #what is contained there
            if space != '.': #since we replaced all reachable positions with numbers, if the space is a '.' it cant be reached by the unit
                num = int(space) #convert the char to an int
                if num < lowestNum: 
                    lowestNum = num #find the lowest possible destination square with the lowest number(dstance from the unit)
        #print(lowestNum)
        
        nearestDestinations = [] #now that we have the lowestNum, add all positions that are that distance from the unit to this array
        for spaceTup in possibleDestinations:
            if gridCopy[spaceTup[0]][spaceTup[1]] == lowestNum:
                nearestDestinations.append(spaceTup)
        print(self)
        print(nearestDestinations)

        if len(nearestDestinations) == 0:
            return None
        destination = nearestDestinations[0] #this is a heuristic, the nearestdestination array should be in reading order already, but if not this is incorrect

        gridCopy2 = copy.deepcopy(grid) #now we have the square we need to go to, we need to find the shortest path to get there, if there are multiple first step should be in reading order

        nextTempSpaceArray = [] #performing the same operation as finding which destination to move to but starting at the destination, to the unit
        gridCopy2[destination[0]][destination[1]] = 'X' #set the detination as an X so its not a '.'
        
        for tup in spaceOptionsArray: #if the destination square is one of the square already in range of the unit, just return that square
            if gridCopy2[tup[0]][tup[1]] == "X":
                return tup

        origBackSpaceArray = self.returnOpenAdjacentSpaces(grid, destination[0], destination[1]) #fill this array to eval positions

        for i in range(1,20): # same thing as above, setting distances on grid = to i, and then adding new squares to eval to nextTempSpaceArray
            for tup in origBackSpaceArray:
                gridCopy2[tup[0]][tup[1]] = i
                nextTempSpaceArray.extend(self.returnOpenAdjacentSpaces(gridCopy2, tup[0], tup[1]))

            origBackSpaceArray = nextTempSpaceArray.copy() #swap arrays
            nextTempSpaceArray = [] #empty next array to be refilled and recopied next iteration

        #print("dest: ", destination)
        #print("options: ", spaceOptionsArray)
        ret_str = "" #display grid
        for row in gridCopy2:
            for elem in row:
                ret_str += str(elem)
            ret_str += '\n'
        #print(ret_str)

        #print(lowestNum)
        for i in range(len(gridCopy2)): #search through the original grid in reading order to find the first 1, which will be the shortest path in reading order
            for j in range(len(gridCopy2[i])): #this may also be a heuristic though
                if ((i,j) in spaceOptionsArray and gridCopy2[i][j] == lowestNum-1):
                    return (i,j)   

game = BattleGrid()

print(game)

game.performUnitActions()
print(game)

game.performUnitActions()
print(game)

userInput = ""
while userInput == "":
    userInput = input()
    game.performUnitActions()
    print(game)
    #print(game.unitReadingOrderArray)

