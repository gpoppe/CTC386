#Garrett Poppe
#lab 4

name = input("enter your name")

time = float(input("enter time using 24 hour"))

if (time < 1200) and (time > 400):
    print("Good morning ", name)
elif (time >1199) and (time < 1700):
    print("Good afternoon ", name)
else:
    print("Good evening ", name)


