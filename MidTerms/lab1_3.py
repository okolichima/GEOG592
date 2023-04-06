#Sample solution for lab1, question 3
ddmmssString = raw_input("Please input a ddmmss value in the format dd:mm:ss.\n")
ddmmssList = ddmmssString.split(":")
dd = float(ddmmssList[0])
mm = float(ddmmssList[1])
ss = float(ddmmssList[2])

decimalValue = dd + mm/60 + ss/3600

print ("The decimal value is "+ str(decimalValue))

