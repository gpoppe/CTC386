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








bit1a = fullbit%10
bit2a = math.floor(fullbit/10)%10
bit3a = math.floor(fullbit/100)%10
bit4a = math.floor(fullbit/1000)%10
bit5a = math.floor(fullbit/10000)%10
bit6a = math.floor(fullbit/100000)%10

print("bit6a=",bit6a," bit5a=",bit5a," bit4a=",bit4a," bit3a=",bit3a," bit2a=",bit2a," bit1a=",bit1a)
total = 0
if(bit1a == 1):
    total = total + 1
if(bit2a == 1):
    total = total + 2
if(bit3a == 1):
    total = total + 4
if(bit4a == 1):
    total = total + 8
if(bit5a == 1):
    total = total + 16
if(bit6a == 1):
    total = total + 32

print("decimal number is ",total)

