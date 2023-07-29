name = input("Welcome to the your own adventure!\nPlease enter you name: ")

ans = input(
    "The jungle was hot and humid, and the air was thick with the sound of insects buzzing.\nYou were on a solo expedition to find the lost city of El Dorado, and you were starting to wonder if I would ever find it.\nDo you still wonder?(yes/no): "
).lower()
if ans == "yes":
    print("Oh no! Your lack of courage has failed you. Try next time, " + name + " .")
elif ans == "no":
    ans = input(
        "You had been trekking through the jungle for days, and You were starting to run low on supplies.\nYou were also starting to get worried about the dangers of the jungle.\nYou had seen jaguars, snakes, and even a few caimans. Do you still was to continue?(yes/no): "
    ).lower()
    if ans == "no":
        print(
            "Oh no! Your lack of determination has failed you. Try next time, "
            + name
            + " ."
        )
    elif ans == "yes":
        ans = input(
            "One day, You were walking through a clearing when you saw something that made your heart skip a beat.\nThere, in the distance, was a city.\nIt was made of gold, and it glistened in the sunlight.\nAre you happy?(yes/no): "
        ).lower()
        if ans == "no":
            print(
                "Oh no! Your lack of satisfaction has failed you. Try next time, "
                + name
                + " ."
            )
        elif ans == "yes":
            print("Congrats! You have found El Dorado. You won, " + name + " .")
        else:
            print("Invalid option! Try next time,  " + name + " .")
    else:
        print("Invalid option! Try next time,  " + name + " .")
else:
    print("Invalid option! Try next time,  " + name + " .")
