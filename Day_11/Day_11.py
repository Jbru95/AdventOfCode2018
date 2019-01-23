'''
Day 11
Part 1 - find the 3x3 grid with the highest total power in the power grid
    Answer - What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with the largest total power? -> 235,22
Part 2 - find the yxy grid with the highest total power across all square grid sizes
    Answer - What is the X,Y,size identifier of the square with the largest total power? -> 231,135,8
    Note - Answers get really really slow past 10, luckily, past 20, all answer come out as 0,0,y, 8 seemed to be the highest and was correct
'''
input_multiplier = 5177

power_grid = []
power_num = 0
power_dict = {}

for i in range(300):
    grid_row = []
    for j in range(300):
        power_num = 0

        power_num += (j + 11)
        power_num *= (i + 1)
        power_num += input_multiplier
        power_num *= (j + 11)

        if power_num < 100:
            power_num = 0
        else:
            power_num = int(str(power_num)[-3])

        power_num -= 5

        power_dict[str(i) + ',' + str(j)] = power_num

        grid_row.append(power_num)

    power_grid.append(grid_row)



def calc_max_power(power_grid, quadrant_size):
    calc_grid = power_grid

    for i in range(300):
        for j in range(300):
            quadrant_power = 0
            try:
                for x in range(quadrant_size):
                    for y in range(quadrant_size):
                        #quadrant_power += power_grid[i+x][j+y]
                        quadrant_power += power_dict[str(i+x) + ',' + str(j+y)]
            except KeyError:
                continue
            
            calc_grid[i][j] = quadrant_power

    top_tup = [0, 0, 0] #(val, x, y)

    for i in range(300 - quadrant_size):
        for j in range(300 - quadrant_size):
            if calc_grid[i][j] > top_tup[0]:
                top_tup[0] = calc_grid[i][j]
                top_tup[1] = j + 1
                top_tup[2] = i + 1

    return top_tup

answer_list = []

for i in range(300):
    print(i)
    print(calc_max_power(power_grid, i))

print(answer_list)




