#Sample script for lab2_4
#In q4.py, please modify q3.py, so you can output a sorted county list,
#based on populate change from 2000-2010, save the output to ncpopchgSorted.txt.
nc2010File = open("NC2010.txt", "r")
ncpopChgFile = open("ncpopchgSorted.txt", "w")
ncpopChgFile.write("County Name, PopChg%\n")

allLines = nc2010File.readlines()[1:]
aCountyRecList = []
for aLine in allLines:
    aListOfTokens = aLine.split(",")
    pop2000 = float(aListOfTokens[6])
    pop2010 = float(aListOfTokens[8])
    popChg = ((pop2010-pop2000)/pop2000)*100
    aCountyRecList.append((aListOfTokens[1], popChg))
    
aSortedList = sorted(aCountyRecList,key=lambda countyRec:countyRec[1])
for aRec in aSortedList:
    ncpopChgFile.write(aRec[0]+","+str(aRec[1])+"\n")
nc2010File.close()
ncpopChgFile.close()
