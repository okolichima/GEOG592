#Sample solution for lab2, question 2
# In q2.py, please ask a user to input a list of numbers, separated by space, then prompt the user with the average,
# median, sum of the list, and also output a sorted list.

aNumberListStr = raw_input("Please input a list of numbers separated by spaces.\n")
aNumStrList = aNumberListStr.split()

aNumList=[]
for aNumStr in aNumStrList:
    aNumList.append(int(aNumStr))
total = 0.0
for aNum in aNumList:
    total += aNum
lenList = len(aNumList)
average = total/lenList

aSortedList = sorted(aNumList)

median = 0
if lenList%2 == 0:
    median = (aSortedList[lenList/2-1]+aSortedList[lenList/2])/2.0
else:
    median = aSortedList[(lenList-1)/2]

print("The average: %s, median: %s, sum: %s" % (average, median, total))

print("The list is :")

print(aSortedList)








