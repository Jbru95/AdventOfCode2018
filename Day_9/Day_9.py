fp = open('test_input.txt', 'r')
inp_list = fp.read().strip().split()
fp.close()

player_num = int(inp_list[0])
last_marble_value = int(inp_list[6])

marble_circle = [0]
player_score_array = []
current_marble_index = 0

for i in range(player_num):
    player_score_array.append(0)

#print(player_score_array)

for i in range(1, last_marble_value + 1):
    if (i % 23 != 0):

        insert_index = current_marble_index + 2
        if ((current_marble_index + 2) >= len(marble_circle)+1):
            insert_index = 1

        marble_circle.insert((insert_index), i)
        #print(current_marble_index + 2)
        current_marble_index = insert_index
        #print(marble_circle)

    else: 
        #print("current index: ", current_marble_index)

        if(current_marble_index - 7 >= 0):
            player_score_array[(i%player_num)] += marble_circle.pop(current_marble_index - 7)
            player_score_array[(i%player_num)] += i
            current_marble_index = current_marble_index - 7
        else:
            player_score_array[(i%player_num)] += marble_circle.pop(len(marble_circle) + (current_marble_index - 7))
            player_score_array[(i%player_num)] += i
            current_marble_index = (len(marble_circle) - (current_marble_index - 7))


player_score_array.sort()
print(player_score_array)

#PART 2 VERY VERY VERY SLOW, NEED 0(1) INSERTION, DOUBLY LINKED LIST WOULD BE IDEAL

