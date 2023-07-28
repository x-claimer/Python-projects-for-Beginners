import random

print(
    "Welcome to the Number guessing game. \nYour task is to guess the whole number in minimum tries."
)

top_val = input("Enter the top value of the range: ")
if top_val.isdigit():
    if int(top_val) <= 0:
        print("Next time, type an integer greater than 0.")
        exit()

    num = random.randrange(int(top_val) + 1)
else:
    print("Next time, type an integer.")
    exit()

tries = 0
while True:
    guessed_num = input("Enter your guess: ")
    tries += 1
    if int(guessed_num) == num:
        print("Congrats! You have guessed the number in " + str(tries) + " tries.")
        break
    elif int(guessed_num) > num:
        print("Your guess is above the number.")
    else:
        print("Your guess is below the number.")
