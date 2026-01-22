#garrett poppe
#github test comment


#function definitions
def scaryfunction():
    print("scary...")
    print("more scary...")
    print("JK 6 or 9")




#main program portion


name = "garrett"
print("    Menu       ")
print("_______________")

print("option 1")
print("option 2")
print("option 3")
print("option 4")
print("option 5")
print("option 6")
print("________________")

print("hello ",name," Enter an option")
x = int(input())

if (x == 1):
    print("you chose option 1")
elif (x == 2):
    print("you chose option 2")
elif (x == 3):
    print("you chose option 3")
elif (x ==4):
    print("welcome to the guessing game")
    guess = 101
    while (guess != 65):
        guess = int(input(" Enter your guess: "))
        #range control for guess
        while (guess < 0) or (guess > 100):
            guess = int(input(" Enter your guess between 1 and 100: "))
            if (guess < 0) or (guess > 100):
                print("your guess is out of range")
        
        if (guess > 65):
            print("Your guess is too high")
        elif (guess < 65):
            print("Your guess is too low")
        else:
            print("congratulations, you guess the number 65")

elif (x == 5):
    print("You chose option 5")

elif (x == 6):
    print("Welcome to the escape room")
    print("You see three doors, choose one...")
    door = int(input())
    if (door == 1):
        for i in range(5):
            print("aaaaaaaaaaahhhhhh monsters!!!")
    elif (door == 2):
        scaryfunction()
    elif (door == 3):
        print(" You have escaped, nice work!")





