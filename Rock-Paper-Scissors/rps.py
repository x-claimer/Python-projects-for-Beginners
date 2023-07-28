import random

print("Lets play Rock/Paper/Scissors. If you want to quit, type 'Quit'.\n")

user_score = 0
comp_score = 0

chances = ["rock", "paper", "scissors"]
# rock=0, paper=1, scissors=2
while True:
    user_inp = input("Enter Rock/Paper/Scissors/Quit: ").lower()

    if user_inp == "quit":
        break
    elif user_inp not in chances:
        continue
    else:
        random_num = random.randrange(2)
        comp_inp = chances[random_num]
        print("Computer picked: " + comp_inp)

        if user_inp == "rock" and comp_inp == "scisscors":
            user_score += 1
            print("You Won!")
        elif user_inp == "scissors" and comp_inp == "paper":
            user_score += 1
            print("You Won!")
        elif user_inp == "paper" and comp_inp == "rock":
            user_score += 1
            print("You Won!")
        elif user_inp == comp_inp:
            print("Its a Draw!")
        else:
            comp_score += 1
            print("You Lost!")

print(
    "Here are the scores, Computer score is "
    + str(comp_score)
    + " and your score is "
    + str(user_score)
    + " ."
)

if user_score > comp_score:
    print("Hurry!! You won the game.")
elif user_score == comp_score:
    print("Oh no! Its a draw.")
else:
    print("Computer won the game. Try next time.")
