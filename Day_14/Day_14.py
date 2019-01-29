
'''
Day 14: Chocolate Charts

2 Elves, making recipes, to create a new one, the 2 elves combine their current recipes, the new recipes scores are the digits of the sum of the 2 current recipes
i.e. 3 and 7 become 10 -> becomes 1 and 0, if only one digit, just creates 1 recipe with that score, new recipes are added to the scoreboard -> 3,7,1,0
To pick new recipes, the elves step forward (1 + current recipe score) times (looping around if they have to)

Part 1 -> Find the scores of the 10 recipes immediately after the number of recipes in your puzzle input (702831)
    - requires a lot of walking through arrays and appending numbers to the end
    - lists should work well, as appending to the end is O(1) and indexing with the calculated new spot should only be O(1)
    - size could be a problem tho as the array will have to grow to 700000+ (may have to come up with a mathematical heuristic)
    - 2164812816 too high
    - 164812816 too low oops
    - 1648128164 too high
    - reworked code to be more generalizeable, also change to be <= 9 for reassigning indicies
        -1132413111 -> correct Answer

Part 2 -> Now find the number of recipes before the input sequence appears, i.e. length before 702831 appears in that order
    - convert the array to a string at the end and then use str.find() to find the answer
    - 20340232


'''

input_num = 702831

scoreboard = [3,7]

one_index = 0
two_index = 1
find_str = ""


def create(scoreboard, one_index, two_index):

    combined_score = scoreboard[one_index] + scoreboard[two_index]
    if combined_score <= 9:
        scoreboard.append(combined_score)
        #find_str += str(combined_score)
    elif combined_score > 9:
        scoreboard.append( int(str(combined_score)[0]))
        scoreboard.append( int(str(combined_score)[1]))
        #find_str += str(combined_score)[0]
        #find_str += str(combined_score)[1]
        
    one_index += (scoreboard[one_index] + 1)
    if one_index > len(scoreboard) - 1:
        one_index = one_index % (len(scoreboard))

    two_index += (scoreboard[two_index] + 1)
    if two_index > len(scoreboard) - 1:
        two_index = two_index % (len(scoreboard))

    return one_index, two_index

while len(scoreboard) < 100000000:
    one_index, two_index = create(scoreboard, one_index, two_index)
    # print(scoreboard)
    # print("elf 1 index: ", one_index, " -> ", scoreboard[one_index] )
    # print("elf 2 index: ", two_index, " -> ", scoreboard[two_index] )

for elem in scoreboard:
    find_str += str(elem)

print(find_str)
print(len(find_str))
print(find_str.find(str(input_num)))




#print(len(scoreboard))
#print(scoreboard[-5:])

# for i in range(10):
#     one_index, two_index = create(scoreboard, one_index, two_index)

#print(scoreboard[input_num:input_num + 10])






