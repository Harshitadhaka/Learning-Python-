import random

score = 0

for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    answer = int(input(f"What is {a} x {b}? "))

    if answer == a * b:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer =", a * b)

print("\nFinal Score =", score, "/ 5")
