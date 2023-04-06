#In q3.py, please find NC2010.txt in lab2 folder first, then calculate the
#population change for each county from 2000-2010, and output the result to
#a textfile ( ncpopchg.txt).
#You could use this output format -
#CountyName, PopChg%
#....
#Orange, 21.11%
#Durham, 17.12%

nc2010File = open("NC2010.txt", "r")
ncpopChgFile = open("ncpopchg.txt", "w")
ncpopChgFile.write("CountyName, PopChg%")

allLines = nc2010File.readlines()[1:]

for aLine in allLines:
    aListOfTokens = aLine.split(",")
    pop2000 = float(aListOfTokens[6])
    pop2010 = float(aListOfTokens[8])
    popChg = ((pop2010-pop2000)/pop2000)*100
    ncpopChgFile.write(aListOfTokens[1]+","+str(popChg)+"\n")


nc2010File.close()
ncpopChgFile.close()
