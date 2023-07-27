print("Welcome to the VALORANT quiz")

initiate = input("Want to have a quiz?[Y/N] ")

if initiate.upper() != "Y":
    print("Thanks for having a thought.")
    exit()

print("Lets start the quiz. You will be asked 10 basic question about Valorant.")

Score = 0

### Question 1
ans1 = input("Which genre valorant belongs to? [Hint: s***t*r] \n")
if ans1.lower() == "shooter":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 2
ans1 = input("How many players can play in each party? \n")
if ans1.lower() == "5":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 3
ans1 = input("How many maps are there in total? \n")
if ans1.lower() == "7":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 4
ans1 = input("How many agents are there in total? \n")
if ans1.lower() == "18":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 5
ans1 = input("Name one dueslist? \n")
if ans1.lower() in ["raze", "jett", "phoenix", "reyna", "yoru", "neon"]:
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 6
ans1 = input("Name one controller? \n")
if ans1.lower() in ["brimstone", "omen", "viper", "astra", "harbor"]:
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 7
ans1 = input("Lowest rank in Valorant with denomination? \n")
if ans1.lower() == "iron 1":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 8
ans1 = input("Highest rank in Valorant? \n")
if ans1.lower() == "radiant":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 9
ans1 = input("Who is developer/publisher of Valorant \n")
if ans1.lower() == "riot games":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

### Question 10
ans1 = input("In which year was Valorant released? \n")
if ans1.lower() == "2020":
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

print("Congrats!! you have completed the quiz. This is your score: " + str(Score))
