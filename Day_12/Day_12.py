'''
Day 12 - Plants in Pots

Part 1 -> propogate the plants after 20 generations, add up the index of all the plants. Answers -> 2995
Part 2 -> propogate the plants after 50 billion generations, add up the index of all the plants. Answer -> 3650000000377
        - obviously this presents a memory problem as itll be a string greater than 50 billion size
        - also the sheer number of iterations is absurd
        - process: propogate over 500 generations and observe the difference in the resltant generations number
                - this stabilizes after about 100 gens, and added 73 to the next gens number, so i did the number after 500 += 37*(50 bil - 500) and got the correct answer
'''

fp = open('input.txt', 'r')
init_str = fp.readline()

init_state = '..........' + init_str[init_str.find(':')+2:-1] + 1000*'.' #10 dots at the beginning are -10 to 0, so counting starts at -10

rule_dict = {}

fp.readline()

for line in fp.readlines():
    rule = line[:5]
    result = line[-2:-1]
    rule_dict[rule] = result

print(init_state)
last_result_num = 0
for j in range(500):

    next_state = '..'
    

    for i in range(2, len(init_state) - 2):

        check_str = init_state[i-2: i+3]

        if check_str in rule_dict: 
            next_state += rule_dict[check_str]

    next_state += '..'
    init_state = next_state
    
    result_num = 0

    for i in range(len(init_state)):
        if init_state[i] == '#':
                result_num += (i-10)


    print('result: ', result_num, ' gen: ', j)
    print('difference from last: ', result_num - last_result_num)
    last_result_num = result_num

result_num += 73*(50000000000-500)
print(result_num)




        
        
        



