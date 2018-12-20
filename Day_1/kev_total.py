
freqArray = []
sum = 0
doubleFreq = 0
doubleFlag = False


while doubleFlag == False:


    f = open("input.txt",'r')
    for line in f.readlines():

        count = 0
        sum = sum + int(line)

        freqArray.append(sum)

        count = freqArray.count(sum)

        if(count == 2):

            doubleFreq = sum

            print(doubleFreq)

            doubleFlag = True

            break

    f.close()
