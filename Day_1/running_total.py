
#Advent_Code Day 1
#Part1: Find a running Total (frequency) of a list of number given in input.txt  
#Part2: Find the first repeating frequency, may have to iterate through the list of numbers many times(over 100 in this case)

#Part1 Ans => 522
#Part2 Ans => 73364

number_ary = []

fp = open('input.txt', 'r')

for line in fp.readlines():
    number_ary.append(int(line))
fp.close()

frequency = 0
frequency_dict = {}
found = False
i = 0

while found == False:
    i += 1
    print(i)
    for num in number_ary:
        frequency += num

        if frequency_dict.get(str(frequency)) == None:
            frequency_dict[str(frequency)] = 1
        else: 
            print(frequency)
            found = True
            break





