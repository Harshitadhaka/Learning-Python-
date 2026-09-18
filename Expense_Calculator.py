food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
shopping = float(input("Enter shopping expense: "))
other = float(input("Enter other expense: "))

total = food + travel + shopping + other

print("\n===== EXPENSE REPORT =====")
print("Food =", food)
print("Travel =", travel)
print("Shopping =", shopping)
print("Other =", other)
print("Total Expense =", total)
