'''
Day 15 - Goblins vs. Elves
'''
import copy
class BattleGrid:
    
    def __init__(self):
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
        ret_str = ""
        for row in self.grid:
            for elem in row:
                ret_str += str(elem)
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
        if game.grid[self.i - 1][self.j] == self.enemyType:
            return (self.i - 1,self.j)
        if game.grid[self.i][self.j-1] == self.enemyType:
            return (self.i,self.j-1)
        if game.grid[self.i][self.j+1] == self.enemyType:
            return (self.i,self.j+1)
        if game.grid[self.i + 1][self.j] == self.enemyType:
            return (self.i+1,self.j)
        return None

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
        print(enemyOpenSpaces, self.inRangeOfEnemy(game))
        if (len(enemyOpenSpaces) == 0) and (self.inRangeOfEnemy(game) == None): #checking to see if any moves are possible
            return None
        
        if(self.inRangeOfEnemy(game) != None): #in range of enemy so attack
            self.attack(game, self.inRangeOfEnemy(game))
    
        else: #enemy has open spaces and there is not an enemy in range so time to move
            moveSpace = self.returnMoveSpace(copy.deepcopy(game.grid), game.goblinUnitArray.copy(), game.elfUnitArray.copy())
            self.move(game, moveSpace)


    def returnMoveSpace(self, grid, goblinArray, elfArray): #return a space to move to, or return None if the unit shouldn't move
        print('in return move space')
        gridCopy = copy.deepcopy(grid)
        spaceOptionsArray = []
        possibleDestinations = []
        spaceOptionsArray.extend(self.returnOpenAdjacentSpaces(gridCopy, self.i, self.j)) #fill array 

        if self.type == "E":
            for unit in goblinArray:
                possibleDestinations.extend(self.returnOpenAdjacentSpaces(gridCopy, unit.i, unit.j))

        if self.type == "G":
            for unit in elfArray:
                possibleDestinations.extend(self.returnOpenAdjacentSpaces(gridCopy, unit.i, unit.j))

        print(spaceOptionsArray, possibleDestinations)

        origTempSpaceArray = copy.deepcopy(spaceOptionsArray)
        nextTempSpaceArray = []
        tupsToDeleteArray = []

        for i in range(1,20):
            for tup in origTempSpaceArray:
                gridCopy[tup[0]][tup[1]] = i
                tupsToDeleteArray.append(tup)
                nextTempSpaceArray.extend(self.returnOpenAdjacentSpaces(gridCopy, tup[0], tup[1]))

            origTempSpaceArray = nextTempSpaceArray.copy()
            nextTempSpaceArray = []

        destinationDistanceDict = {}
        lowestNum = 1000
        for spaceTup in possibleDestinations:
            space = gridCopy[spaceTup[0]][spaceTup[1]]
            if space != '.':
                num = int(space)
                if num < lowestNum:
                    lowestNum = num
        print(lowestNum)
        
        nearestDestinations = []
        for spaceTup in possibleDestinations:
            if gridCopy[spaceTup[0]][spaceTup[1]] == lowestNum:
                nearestDestinations.append(spaceTup)
        print(self)
        destination = nearestDestinations[0] #this is a heuristic, the nearestdestination array should be in reading order already, but if not this is incorrect
        gridCopy2 = copy.deepcopy(grid)

        nextTempSpaceArray = []
        tupsToDeleteArray = []
        gridCopy2[destination[0]][destination[1]] = 'X'
        
        for tup in spaceOptionsArray:
            if gridCopy2[tup[0]][tup[1]] == "X":
                return tup

        origBackSpaceArray = self.returnOpenAdjacentSpaces(grid, destination[0], destination[1])

        for i in range(1,20):
            for tup in origBackSpaceArray:
                gridCopy2[tup[0]][tup[1]] = i
                tupsToDeleteArray.append(tup)
                nextTempSpaceArray.extend(self.returnOpenAdjacentSpaces(gridCopy2, tup[0], tup[1]))

            origBackSpaceArray = nextTempSpaceArray.copy()
            nextTempSpaceArray = []

        #print("dest: ", destination)
        #print("options: ", spaceOptionsArray)
        ret_str = ""
        for row in gridCopy2:
            for elem in row:
                ret_str += str(elem)
            ret_str += '\n'
        #print(ret_str)  

        #print(lowestNum)
        for i in range(len(gridCopy2)):
            for j in range(len(gridCopy2[i])):
                if ((i,j) in spaceOptionsArray and gridCopy2[i][j] == lowestNum-1):
                    return (i,j)   

game = BattleGrid()

print(game)
print(game.grid)
print(game.unitReadingOrderArray)
print(game.unitDict)


for i in range(20):
    game.performUnitActions()
    print(game)
    print(game.unitReadingOrderArray)
