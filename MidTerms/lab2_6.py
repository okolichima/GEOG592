# Sample solution for lab2 question 6

cityFile = open("Cities.txt","r")
locationFile = open("Locations.txt","r")

cityLines = cityFile.readlines()[1:]
locationLines = locationFile.readlines()[1:]
locationList = []

for aLocation in locationLines:
    sumDistance = 0
    locationFlds = aLocation.split(",")
    locationX = float(locationFlds[1])
    locationY = float(locationFlds[2])
    for aCity in cityLines:
        cityFlds = aCity.split(",")
        cityX = float(cityFlds[1])
        cityY = float(cityFlds[2])
        dist = ((locationX-cityX)**2+(locationY-cityY)**2)**.5
        sumDistance += dist
    locationList.append((locationFlds[0], sumDistance))

sortedLocationList = sorted(locationList, key = lambda locationRec:locationRec[1])

print("The best location id is %s" % sortedLocationList[0][0])
print("The best average distance is " + str(sortedLocationList[0][1]/(5240*len(cityLines))))

cityFile.close()
locationFile.close()

                        
