#Garrett Poppe
#Lab 5

number = 7
guess = 0


while (guess != number):
    guess = int(input("Guess the magic number"))
    if (guess != number):
        print("Sorry, try again.")

print("You won, good guess!")


