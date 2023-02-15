#!/usr/bin/python3


vegeta= 0
goku= 0
gohan= 0
piccolo= 0

while True: # this loop won't end under the user types in a,b,c, or d

    q1= input("""What is your favorite color?
                     A. blue
                     B. orange
                     C. purple
                     D. green
                 >""")

    if q1 == "a":
        vegeta += 1
    elif q1 == "b":
        goku += 1
    elif q1 == "c":
        gohan += 1
    elif q1 == "d":
        piccolo += 1
    if q1 in ["a","b","c","d"]:
        break   # if the user gives an appropriate answer, the while loop ends
    else:
        print("You must select A, B, C, or D!") # if an appropriate answer is NOT given, we scold the user and the while loop begins again

# this won't be part of the while loop-- meaning it won't get repeated over. it will display AFTER the user gives a valid answer
print("VEGETA=", vegeta)
print("GOKU=", goku)
print("Gohan=", gohan)
print("Piccolo=", piccolo)
