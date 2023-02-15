#!/usr/bin/python3

print("Which DBZ Character Are You?")

# lets start by making variables to hold our "scores" for each character
vegeta= 0
goku= 0
gohan= 0
piccolo= 0

while True: # this loop won't end unless the user types in a,b,c, or d

# at the start, they're all at zero of course

# now we'll ask a question:
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

   break # if the user gives an appropriate answer, the while loopends
   else:
print("You must select A, B, C, or D!") # if an appropriate answer is NOT given, we scold the user and the while loop begins again

print("VEGETA=", vegeta)
print("GOKU=", goku)
print("Gohan=", gohan)
print("Piccolo=", piccolo)

q2= input("""What is your personality?
                  A. serious and quiet
                  B. enthusiastic and creative
                  C. quiet and idealistic
                  D. independent and determined
         >""")

if q2 == "a":
    vegeta += 1
elif q2 == "b":
    goku += 1
elif q2 == "c":
    gohan += 1
elif q2 == "d":
    piccolo += 1

print("VEGETA=", vegeta)
print("GOKU=", goku)
print("GOHAN=", gohan)
print("PICCOLO=", piccolo)

q3= input("""What motivates you?
                 A. friendly competition
                 B. a good fight
                 C. bullies
                 D. reassurance
         >""")

if q3 == "a":
    vegeta += 1
elif q3 == "b":
    goku += 1
elif q3 == "c":
    gohan += 1
elif q3 == "d":
    piccolo += 1

print("VEGETA=", vegeta)
print("GOKU=", goku)
print("GOHAN=", gohan)
print("PICCOLO=", piccolo)


