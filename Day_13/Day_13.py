'''
Day 13 -> Carts and Crashes
    Part 1 -> Need to model a set of carts and a rail system that the carts move on with certain rules, need to find coordinates of the first crash, denoted by X on the grid
        Answer -> 94,78
    Part 2 -> Instead of carts crashing, when they do they are removed right before a collision, where is the last carts location when it becomes the last cart.
        - last few inputs
            [x: 66, y: 140, disp: <, x: 62, y: 140, disp: >, x: 63, y: 51, disp: ^]
            [x: 65, y: 140, disp: <, x: 63, y: 140, disp: >, x: 63, y: 50, disp: >]
            [x: 64, y: 140, disp: X, x: 64, y: 50, disp: >]
            [x: 65, y: 50, disp: >]
        - Tried -> 64,50  ,  65,50,   63,50    ,   66,50, correct answer -> (26,85)

'''

class Grid:

    def __init__(self):
        fp = open('input.txt', 'r')
        self.grid_array = []
        for line in fp.readlines():
            line = line.rstrip()
            row_array = []
            for i in range(len(line)):
                row_array.append(line[i])
            self.grid_array.append(row_array)
        fp.close()

        self.emptyGrid = [] #cant use assignment of shallow copy via .copy()

        fp2 = open('input_blank.txt', 'r')
        for line in fp2.readlines():
            line = line.rstrip()
            row_array = []
            for i in range(len(line)):
                row_array.append(line[i])
            self.emptyGrid.append(row_array)
        fp2.close()

        # for i in range(len(self.grid_array)):
        #     temp_row = []
        #     for j in range(len(self.grid_array[i])):
        #         temp_row.append(self.grid_array[i][j])
        #     self.emptyGrid.append(temp_row)
                
        # for i in range(len(self.grid_array)):
        #     for j in range(len(self.grid_array[i])):
        #         if self.grid_array[i][j] in ['v','^']:
        #             self.emptyGrid[i][j] = '|'
        #         elif self.grid_array[i][j] in ['<', '>']:
        #             self.emptyGrid[i][j] = '-'

        #for row in self.grid_array:
            #print(row)

        self.cartArray = []

        for i in range(len(self.grid_array)):
            for j in range(len(self.grid_array[i])):
                if self.grid_array[i][j] in ['<','>','^','v']:
                    self.cartArray.append(Cart(j,i,self.grid_array[i][j]))
        print(self.cartArray)


    def displayGrid(self):
        print_str = ""
        for i in range(len(self.grid_array)):
            for j in range(len(self.grid_array[i])):
                print_str += self.grid_array[i][j]
            print_str += '\n'
        print(print_str)
        for cart in self.cartArray:
            print(cart)

    def moveCarts(self):
        for cart in self.cartArray:
            cart.move_cart(self.grid_array, self.cartArray)
            self.updateCartLocations()
        self.removeCrashedCarts()

    def updateCartLocations(self):
        emptyGrid = self.emptyGrid

        for cart in self.cartArray:
            emptyGrid[cart.y][cart.x] = cart.cartDisplay
        
        self.grid_array = emptyGrid

        self.emptyGrid = [] #cant use assignment of shallow copy via .copy()

        fp2 = open('input_blank.txt', 'r')
        for line in fp2.readlines():
            line = line.rstrip()
            row_array = []
            for i in range(len(line)):
                row_array.append(line[i])
            self.emptyGrid.append(row_array)
        fp2.close()
        
    def removeCrashedCarts(self):
        for cart in self.cartArray: 
            if cart.cartDisplay == 'X':
                self.cartArray.remove(cart)



class Cart: 

    def __init__(self, rowIndex, columnIndex, cartDisplay):
        self.cartDisplay = cartDisplay
        self.turnIndex = 0
        self.y = columnIndex
        self.x = rowIndex
        self.turnArray = ['left', 'straight', 'right']

    def __repr__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", disp: " + self.cartDisplay

    def move_cart(self, grid, cartArray):
        #print(self)
        if self.cartDisplay == '<':
            if grid[self.y][self.x-1] == '-':
                self.x -= 1

            elif grid[self.y][self.x-1] == '\\':
                self.x -= 1
                self.cartDisplay = '^'

            elif grid[self.y][self.x-1] == '/':
                self.x -= 1
                self.cartDisplay = 'v'

            elif grid[self.y][self.x-1] == '+':
                self.x -= 1
                if self.turnArray[self.turnIndex] == "left":
                    self.cartDisplay = 'v'
                elif self.turnArray[self.turnIndex] == "right":
                    self.cartDisplay = '^'
                self.incrementTurnIndex()
            
            elif grid[self.y][self.x-1] in ['<','>','v','^', 'X']:
                self.x -= 1
                self.cartDisplay = 'X'
                for cart in cartArray:
                    if cart.x == self.x and cart.y == self.y:
                        cart.cartDisplay = "X"

            

        elif self.cartDisplay == '>':
            if grid[self.y][self.x+1] == '-':
                self.x += 1

            elif grid[self.y][self.x+1] == '\\':
                self.x += 1
                self.cartDisplay = 'v'

            elif grid[self.y][self.x+1] == '/':
                self.x += 1
                self.cartDisplay = '^'

            elif grid[self.y][self.x+1] == '+':
                self.x += 1
                if self.turnArray[self.turnIndex] == "left":
                    self.cartDisplay = '^'
                elif self.turnArray[self.turnIndex] == "right":
                    self.cartDisplay = 'v'
                self.incrementTurnIndex()

            elif grid[self.y][self.x+1] in ['<','>','v','^', 'X']:
                self.x += 1
                self.cartDisplay = 'X'
                for cart in cartArray:
                    if cart.x == self.x and cart.y == self.y:
                        cart.cartDisplay = "X"

            
        elif self.cartDisplay == '^':
            if grid[self.y-1][self.x] == '|':
                self.y -= 1

            elif grid[self.y-1][self.x] == '\\':
                self.y -= 1
                self.cartDisplay = '<'

            elif grid[self.y-1][self.x] == '/':
                self.y -= 1
                self.cartDisplay = '>'

            elif grid[self.y-1][self.x] == '+':
                self.y -= 1
                if self.turnArray[self.turnIndex] == "left":
                    self.cartDisplay = '<'
                elif self.turnArray[self.turnIndex] == "right":
                    self.cartDisplay = '>'
                self.incrementTurnIndex()

            elif grid[self.y-1][self.x] in ['<','>','v','^', 'X']:
                self.y -= 1
                self.cartDisplay = 'X'
                for cart in cartArray:
                    if cart.x == self.x and cart.y == self.y:
                        cart.cartDisplay = "X"


        elif self.cartDisplay == 'v':
            if grid[self.y+1][self.x] == '|':
                self.y += 1

            elif grid[self.y+1][self.x] == '\\':
                self.y += 1
                self.cartDisplay = '>'

            elif grid[self.y+1][self.x] == '/':
                self.y += 1
                self.cartDisplay = '<'

            elif grid[self.y+1][self.x] == '+':
                self.y += 1
                if self.turnArray[self.turnIndex] == "left":
                    self.cartDisplay = '>'
                elif self.turnArray[self.turnIndex] == "right":
                    self.cartDisplay = '<'
                self.incrementTurnIndex()

            elif grid[self.y+1][self.x] in ['<','>','v','^', 'X']:
                self.y += 1
                self.cartDisplay = 'X'
                for cart in cartArray:
                    if cart.x == self.x and cart.y == self.y:
                        cart.cartDisplay = "X"
                print("collision occured at X: ", self.x, ", Y: ", self.y)

        #elif self.cartDisplay == "X":
            #continue
            # do nothing

    def incrementTurnIndex(self):
        if self.turnIndex == 2:
            self.turnIndex = 0
        else:
            self.turnIndex += 1


grid = Grid()
grid.displayGrid()

user_input = ""
while user_input == "":

    # if len(grid.cartArray) == 3:
    #     user_input = input()

    if len(grid.cartArray) == 1:
        user_input = input()

    grid.moveCarts()
    print(grid.cartArray)
    grid.displayGrid()
