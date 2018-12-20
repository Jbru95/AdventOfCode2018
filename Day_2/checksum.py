#AdventCode Day 2
#Part1 => generating checksums from id strings, calced as multiplying number of ids with excatly 2 similar letters * number of ids with excatly 3 similar letters
#Part2 => of all IDs, need to find the 2 ids that differ by only one character ie: 'abcde' and 'abxde', and return the common letters => 'abde'

#Answers
#Part1 => 247 * 25 = 6175
#Part2 => asgwjcmzroedihqoutcylvzinx and asgwjcmzrkedihqoutcylvzinx, matching letters => asgwjcmzredihqoutcylvzinx
 
id_array = []
char_dict = {}

appear_twice_count = 0
appear_thrice_count = 0

fp = open('input.txt', 'r')

for line in fp.readlines():
    id_array.append(line)
fp.close()

for line in id_array:
    twice_bool = False
    thrice_bool = False
    char_dict.clear()
    for char in line:
        if char_dict.get(char) == None:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    for vals in char_dict.values():
        if vals == 2 and twice_bool == False:
            appear_twice_count += 1
            twice_bool = True
        if vals == 3 and thrice_bool == False:
            appear_thrice_count += 1
            thrice_bool = True

print(appear_thrice_count, appear_twice_count)
checksum = appear_thrice_count * appear_twice_count
print(checksum)

different_chars = 0

for line in id_array:  #time complexity O(n^2*i) => pretty bad
    for line2 in id_array: 
        for i in range(len(line)):
            if line[i] != line2[i]:
                different_chars += 1
        
        if different_chars == 1:
            match_line = line
            match_line2 = line2
            break
        
        else: 
            different_chars = 0

answer_str = ""

for i in range(len(match_line)):
    if match_line[i] == match_line2[i]:
        answer_str += match_line[i]

print(answer_str)