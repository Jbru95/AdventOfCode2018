'''
non-chronologically ordered guard posts with time stamp, and whether a guard fell asleep or woke up, or whether a certain guard began their shift
    - each guard has an id i.e.
        [1518-11-01 00:00] Guard #10 begins shift
        [1518-11-01 00:05] falls asleep
        [1518-11-01 00:25] wakes up
    - all sleep and awake times are during the midnight hour => 00:00 to 00:59
        -count as asleep the minute that fall asleep and count as awake on the first minute they wake up

    challenge 1: Find the guard that has the most minutes asleep, what minute does that guard fall asleep the mostt
        answer => (guard id) * (most common fall asleep minute)

        will need to keep a collection of the data recorded and then organize them
        array of arrays => [
            [date, time, event], ...
        ]
        answer => (3041)*(29) => 

    challenge 2: Find the guard that is most frequently asleep at the same minute, need the minute and the guard id

        answer => (1997)*(17) =>

'''

fp = open('input.txt','r')

big_array = []


for line in fp.readlines():
    small_array = []
    date = line[1:line.find(' ')]
    time = line[line.find(' ') + 1: line.find(']')]
    event = line[line.find(']') + 2:-1]

    small_array.append(date)
    small_array.append(time)
    small_array.append(event)




    big_array.append(small_array)

big_array.sort()
guard_dict = {}

guard_id = 0
fall_asleep_minute = 0
wake_up_minute = 0
sleep_minutes = 0
guard_3041_array = []
guard_set = set()
for elem in big_array:
    #print(elem)
    if(elem[2][0] == 'G'):
        guard_id = elem[2][elem[2].find('#') + 1:elem[2].find('b')]
        guard_set.add(guard_id)

    elif(elem[2][0] == 'f'):
        fall_asleep_minute = int(elem[1][3:])
    
    elif(elem[2][0] =='w'):
        wake_up_minute = int(elem[1][3:])
        if(guard_id in guard_dict):
            guard_dict[guard_id] += (wake_up_minute - fall_asleep_minute)
        else:
            guard_dict[guard_id] = (wake_up_minute - fall_asleep_minute)
    
    if(guard_id == "3041 "):
        guard_3041_array.append(elem)

print(guard_set)
#print(guard_dict.keys())
#guard 3041 was asleep the longest time
minute_dict = {} #1031, 2221, 3167

for elem in guard_3041_array:

    if(elem[2][0] == 'f'):
        fall_asleep_minute = int(elem[1][3:])

    elif(elem[2][0] =='w'):
        wake_up_minute = int(elem[1][3:])
        for i in range(fall_asleep_minute, wake_up_minute):
            if i in minute_dict:
                minute_dict[i] += 1
            else:
                minute_dict[i] = 1

biggest = 0
for elem in minute_dict.values():
    if elem > biggest:
        biggest = elem

print(3041*39) #guard id was 3041, the MINUTE he spent the most time asleep (16 times) was 39



#guard_dict => maps guard id to number of minutes asleep for that guard, 
#need to map guard to the minute he spent the most time asleep on

guard_dict_max_minutes = {}

for elem in guard_set:
    guard_dict_max_minutes[elem] = {}


temp_minute_dict = {}
guard_id2 = ''
fall_asleep_minute = 0
wake_up_minute = 0
for elem in big_array:
    #print(elem)
    if(elem[2][0] == 'G'):
        guard_id2 = elem[2][elem[2].find('#') + 1:elem[2].find('b')]

    if(elem[2][0] == 'f'):
        fall_asleep_minute = int(elem[1][3:])

    elif(elem[2][0] =='w'):

        temp_minute_dict = guard_dict_max_minutes[guard_id2]


        wake_up_minute = int(elem[1][3:])
        for i in range(fall_asleep_minute, wake_up_minute):
            if i in temp_minute_dict:
                temp_minute_dict[i] += 1
            else:
                temp_minute_dict[i] = 1

        guard_dict_max_minutes[guard_id2] = temp_minute_dict


for tup in guard_dict_max_minutes.items():
    minute_dict = tup[1]

    highest_minute_tup = (0,0)

    for tup2 in minute_dict.items():
        if(tup2[1] > highest_minute_tup[1]):
            highest_minute_tup = tup2

    guard_dict_max_minutes[tup[0]] = highest_minute_tup

for elem in guard_dict_max_minutes.items():
    print(elem)


print(1997*17)






##################################################################################################
#if they wake up, get the dict for the times they slept   {guard : {15:2, 16:1}} 
    




    