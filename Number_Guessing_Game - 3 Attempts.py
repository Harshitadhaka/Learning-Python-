import random

secret_number = random.randint(1, 20)

for attempt in range(3):
    guess = int(input("Guess the number (1-20): "))

    if guess == secret_number:
        print("Correct! You Win!")
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")

else:
    print("You lost!")
    print("The correct number was:", secret_number)
