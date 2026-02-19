#garrett poppe
#github test comment
import math
import random



bit1= int(input("Enter Most Significant bit:"))
bit2 = int(input("Enter Least Significant bit:"))
fullbit = int(input("Enter entire bit string:"))



if (bit1 == 0 and bit2 == 0):
    print("Your decimal number is 0")
elif (bit1 == 0 and bit2 == 1):
    print("your decimal number is 1")
elif (bit1 == 1 and bit2 == 0):
    print("Your decimal nubmer is 2")
elif (bit1 == 1 and bit2 == 1):
    print("Your decimal number is 3")
else:
    print("you must have made a mistake")


