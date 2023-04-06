#Sample solution for lab1, question 4

import itertools

solutionTxt=open("solutions.txt", "w")
counter = 0
for aList in itertools.permutations("123456789",9):
        a = int(aList[0])
        b = int(aList[1])
        c = int(aList[2])
        d = int(aList[3])
        e = int(aList[4])
        f = int(aList[5])
        g = int(aList[6])
        h = int(aList[7])
        i = int(aList[8])
        if (a*100 + b*10 + c) + (d*100 + e*10+ f) == (g*100 + h*10 + i):
                counter = counter + 1
                solutionTxt.write("Solution " + str(counter) + str(aList) + "\n")
                print aList
solutionTxt.close()
print ("The total number of solution is %s " % counter)
