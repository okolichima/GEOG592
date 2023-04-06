#Sample Solution for lab1 - q1

weight = float(raw_input("Please input your weigh here in lbs.\n"))
height = float(raw_input("Please input your height here in decimal feet.\n"))

sw = (height*30.48-105)/0.454

if weight>sw*1.2:
    print("Need urgent weight control.")
elif weight<sw*0.8:
    print("Need to eat more - too slim is also dangours.")
elif weight<sw*0.9 and weight>sw*0.8:
    print("You are healthy, but can still enjoy a little more food.")
elif weight<sw*1.2 and weight>sw*1.1:
    print("Not urgent, but can consider less food and more sports.")
else:
    print("Your weight is within the normal range.")

print("Your standard weight is %f" % sw)
