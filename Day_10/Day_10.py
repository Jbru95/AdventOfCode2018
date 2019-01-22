
class StarMap:
    def __init__(self, length):
        self.starMapArray = []
        self.length = length
        self.starArray = []

        for i in range(self.length):
            tempArray = []
            for j in range(self.length*3):
                tempArray.append('.')
            self.starMapArray.append(tempArray)

    def addStar(self, starToAdd):
        self.starArray.append(starToAdd)

    def display(self):
        self.updateStarMap()
        for i in range(self.length):
            line = ""
            for j in range(self.length*3):
                line += self.starMapArray[i][j]
            print(line)

    def updateStarMap(self):
        self.starMapArray = []
        for i in range(self.length):
            tempArray = []
            for j in range(self.length*3):
                tempArray.append('.')
            self.starMapArray.append(tempArray)

        for star in self.starArray:
            try:
                self.starMapArray[star.ypos][star.xpos] = '#'
            except IndexError:
                continue


    def moveStars(self):
        for star in self.starArray:
            star.move()


class Star: 
    def __init__(self, xpos, ypos, xvel, yvel):

        if xpos > 0:
            self.xpos = xpos%10000 + 100
        else:
            self.xpos = (10000 - (xpos % 10000))*-1 + 100

        if ypos > 0:
            self.ypos = ypos%10000 + 100
        else:
            self.ypos = 10000 - (ypos % 10000) + 100 

        self.xvel = xvel
        self.yvel = yvel

    def move(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

    def __repr__(self):
        ret_str = "current position: (" + str(self.xpos) + ',' + str(self.ypos) + "), vel: <" + str(self.xvel) + ',' + str(self.yvel) + '>'
        return ret_str



starMap = StarMap(200)

fp = open('input.txt', 'r')

for line in fp.readlines():
    velSubStr = line[line.find('v'):]
    
    tempStar = Star( 
        int(line[line.find('<') + 1: line.find(',')]), 
        int(line[line.find(',') + 1: line.find('>')]), 
        int(velSubStr[velSubStr.find('<') + 1: velSubStr.find(',')]), 
        int(velSubStr[velSubStr.find(',') + 1: velSubStr.find('>')])
    )

    starMap.addStar(tempStar)
fp.close()

starMap.updateStarMap()

user_input = ""


for i in range(550):
    starMap.moveStars()

print('movingStars')
while user_input == "":
    user_input = input()
    for i in range(2):
        starMap.moveStars()

    for star in starMap.starArray:
        print(star)
    
    starMap.display()



