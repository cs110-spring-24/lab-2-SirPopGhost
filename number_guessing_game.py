import random
num = random.randint(1, 100)
user = 0
user_count = 0
while user != num:
    user_count += 1
    user = input("Enter your guess: ")
    user = int(user)

    if user > num:
        print("Too high, it was")
    elif user < num:
        print("Too low, it was")
    else:
        print("You got it!")
        print(f"You have guessed {user_count} amount of times.")
        input_user = input("Do you want to go again? Type y if yes. ")
        if input_user == "y":
            num = random.randint(1, 100)
            user = 0
            user_count = 0
        else:
            print("Goodbye!")
            break

