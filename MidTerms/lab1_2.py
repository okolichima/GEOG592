# Sample solution for lab1 question 2
import random
aNumber = random.randint(1,100)

count = 1

while True:
    aGuess = int(raw_input("Please input a number between 1 and 100.\n"))

    if aGuess>aNumber:
        print("Try  low.")
    elif aGuess<aNumber:
        print("Try high.")
    else:
        print("Congratulation! You got the number in %s attempts" % count)
        break
    count += 1


