'''
Advent of Code: Day 3

Part 1, giant 2D array(1000x1000) of cloth, list of portions of the cloth, find the number of inches that are claimed by at least 2 portions
    -Approach:
        -Make a 1000x1000 array of 0s, loop through the list of swatches, increment those numbers by 1, any index with a number greater than 1 would satisfy the requirements
    - #1 @ 817,273: 26x26
        -#1 => id number
        - 817,273 => x and y values of the upper left corner of the swatch, => second is y index, first is x index => [y][x]
        - 26x26 => dimensions of the swatch
    - Worked: Answer was 116489


Part2, which claimed swatch of cloth does not overlap with the others
    -Could take the filled cloth array as it is, recheck all of the claims, if one claim has all 1s, its the correct one, return the id
    -did it, correct: answer was #1260
'''

class Cloth: 

    def __init__(self):
        self.init_array()


    #helper function to initialize arrary that represents cloth
    def init_array(self):
        cloth_array = []
        for i in range(1000):
            small_array = []
            for j in range(1000):
                small_array.append(0)
            cloth_array.append(small_array)
        self.cloth_array = cloth_array


    def count_taken_cloths(self):
        count = 0 
        for i in range(len(self.cloth_array)):
            for j in range(len(self.cloth_array[0])):
                if self.cloth_array[i][j] > 1:
                    count += 1

        return count  

    def parse_inputs(self, input_string): #  '#1 @ 817,273: 26x26'
        x_val = int(input_string[(input_string.find('@')+1):input_string.find(':')].split(',')[0])
        y_val = int(input_string[(input_string.find('@')+1):input_string.find(':')].split(',')[1])
        width = int(input_string[(input_string.find(':')+1):].split('x')[0])
        height = int(input_string[(input_string.find(":")+1):].split('x')[1])
        #print('xval:', x_val, " yval: ", y_val, " x_dim: ", x_dim, " ydim: ", y_dim)

        for i in range(y_val, y_val + height):
            for j in range(x_val, x_val + width):
                self.cloth_array[i][j] += 1

    def find_unique_patch(self, input_string):
        claim_id = input_string[input_string.find('#'):input_string.find('@')]
        x_val = int(input_string[(input_string.find('@')+1):input_string.find(':')].split(',')[0])
        y_val = int(input_string[(input_string.find('@')+1):input_string.find(':')].split(',')[1])
        width = int(input_string[(input_string.find(':')+1):].split('x')[0])
        height = int(input_string[(input_string.find(":")+1):].split('x')[1])

        unique_bool = True
        for i in range(y_val, y_val + height):
            for j in range(x_val, x_val + width):
                if self.cloth_array[i][j] != 1:
                    unique_bool = False
        if unique_bool == True:
            print(claim_id)


cloth_array = []
for i in range(1000):
    small_array = []
    for i in range(1000):
        small_array.append(0)
    cloth_array.append(small_array)


fp = open('input.txt','r')

cloth_obj = Cloth()

for line in fp.readlines():
    cloth_obj.parse_inputs(line)
fp.close()

print(cloth_obj.count_taken_cloths())

fp2 = open('input.txt','r')

for line in fp2.readlines():
    cloth_obj.find_unique_patch(line)
fp2.close()







