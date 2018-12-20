'''
Day 5: Polymer Reduction

    Input is a big chain of chars
        chars with opposite case next to each other are destroyed: repeat this until no more destructions can be made
        answer is the length of the remaining string: polymer => 10599, subtracted 1, is 10598

    part2: seems one type of unit is disrupting the length, try getting rid of each pair of units (a,A) indivdually and seeing what the length is after fully reducing
    answer -> ('j', 5312)

'''

def reduce(polymer_string):
    num_changes = 1

    while num_changes != 0:
        num_changes = 0
        for i in range(0,len(polymer_string)):
            if( (i+1) < len(polymer_string)):
                #print(((polymer_string[i].islower() and polymer_string[i+1].isupper()) or (polymer_string[i].isupper() and polymer_string[i+1].islower())) and (polymer_string[i].lower() == polymer_string[i+1].lower()))
                if(  ((polymer_string[i].islower() and polymer_string[i+1].isupper()) or (polymer_string[i].isupper() and polymer_string[i+1].islower())) and (polymer_string[i].lower() == polymer_string[i+1].lower())):

                    polymer_string_1 = polymer_string[:i]
                    polymer_string_2 = polymer_string[i+2:]
                    polymer_string = polymer_string_1 + polymer_string_2
                    num_changes += 1
    return (len(polymer_string)), polymer_string 


aplha_str = 'qwertyuioplkjhgfdsamnbvcxz'
polymer_string = ""
fp = open('input.txt', 'r')
polymer_string = fp.read()
fp.close()


print(len(polymer_string))

answer1, resultant_polymer = reduce(polymer_string)
print(answer1)

polymer_length_dict = {}
for char in aplha_str: 
    print(char)
    change_polymer = resultant_polymer
    replace_string = change_polymer.replace(char, '')
    replace_string_2 = replace_string.replace(char.upper(), '')

    polymer_length_dict[char] = reduce(replace_string_2)[0]

print(polymer_length_dict)
smallest = 9999999999
for num in polymer_length_dict.items():
    if num[1] < smallest:
        smallest = num[1]
        answer = num

print(answer) 
#naswer was ('j', 5313)
#subtract one from length => 5312 correct!

    






