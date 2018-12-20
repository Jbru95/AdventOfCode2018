'''

infinite grid, with a number of locations on it(input.txt); these extend infinitely, find the largest finite area, points that have the same manhattan distance from 2+ points do not count

    answer => area given by 'b' in output.txt(check it out, its very cool) => 'b' => 5626

part 2:
    find the size of the area where the added manhattan distance from that point to all coordinates is less than 10000
    size => 46554
'''

def calc_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) 

grid = []
for i in range(400):
    row = []
    for j in range(400):
        row.append(0)
    grid.append(row)


fp = open('input.txt', 'r')
alpha = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm."
count = 0
coord_dict = {}
for line in fp.readlines():
    coord= line.strip().split(',')
    coord_dict[alpha[count]] = (int(coord[0]), int(coord[1]))
    grid[int(coord[0])][int(coord[1])] = alpha[count]
    count += 1
fp.close()

for row in grid:
    for elem in row:
        print(elem, end="")
    print()

print(coord_dict)

smallest_dist = 999999
for i in range(400):
    for j in range(400):
        smallest_dist = 999999
        for tup in coord_dict.items():
            if calc_manhattan_distance(tup[1],(i,j)) < smallest_dist:
                smallest_dist = calc_manhattan_distance(tup[1],(i,j))
                smallest_key = tup[0]
                tie_flag = False

            elif calc_manhattan_distance(tup[1],(i,j)) == smallest_dist:
                tie_flag = True

        if tie_flag == False:
            grid[i][j] = smallest_key
        else:
            grid[i][j] = '.'

#for tup in coord_dict.items():
    #grid[tup[1][0]][tup[1][1]] = tup[0]

'''
fp2 = open('output.txt', 'w')
for row in grid:
    for elem in row:
        print(elem, end="")
        fp2.write(elem)
    print()
    fp2.write('\n')
'''

count_dictionary = {}
for char in alpha:
    count_dictionary[char] = 0
exclude_set = set()
for i in range(400):
    for j in range(400):
        count_dictionary[grid[i][j]] += 1

        if(i == 0 or j == 0 or i == 399 or j == 399):
            exclude_set.add(grid[i][j])
        

print(count_dictionary)
print(exclude_set)


#part 2

for i in range(400):
    for j in range(400):
        accumulated_distance = 0
        for tup in coord_dict.items():
            accumulated_distance += calc_manhattan_distance(tup[1],(i,j))
        
        if accumulated_distance < 10000:
            grid[i][j] = "#"
        else:
            grid[i][j] = "."

hash_area = 0
for i in range(400):
    for j in range(400):
        if(grid[i][j] == "#"):
            hash_area += 1

print(hash_area)
