score = 0

print("===== PYTHON QUIZ =====")

answer = input("1. Which language are we learning? ").lower()

if answer == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. Which symbol is used for comments in Python? ")

if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour Score =", score, "/ 3")
