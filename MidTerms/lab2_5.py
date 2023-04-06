# Sample solution for lab4 question 5
#(5) Given two list of coordinates -
#list1 =[(10,20),(25,8),(34,22),(17,35),(9,1),(31,20),(44,11)]
#list2 = [(1,21),(19,22),(23,12),(51,26),(78,61),(41,17),(11,21),(81,10),(79,51)]
#In your q5.py, please find the mean center of both point lists and output the
#value; please find the average distance between a point in list1 and a point
#in list2.

def meanCenter(aListPts):
    aX = 0.0
    aY = 0.0
    for aPoint in aListPts:
        aX += aPoint[0]
        aY += aPoint[1]
    numPts = len(aListPts)
    return(aX/numPts, aY/numPts)
list1 =[(10,20),(25,8),(34,22),(17,35),(9,1),(31,20),(44,11)]
list2 = [(1,21),(19,22),(23,12),(51,26),(78,61),(41,17),(11,21),(81,10),(79,51)]
mc1 = meanCenter(list1)
mc2 = meanCenter(list2)
print ("Mean center of list1 is ("+str(mc1[0])+","+str(mc1[1])+")\n")
print ("Mean center of list2 is ("+str(mc2[0])+","+str(mc2[1])+")\n")

totalDist = 0
for aPoint in list1:
    for bPoint in list2:
        dist = ((aPoint[0]-bPoint[0])**2 + (aPoint[1]-bPoint[1])**2)**.5
        totalDist += dist
averageDist = totalDist/(len(list1)*len(list2))
print ("Average distance is %s" % averageDist)
