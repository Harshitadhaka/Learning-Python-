balance = 5000

print("===== ATM =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Your Balance =", balance)

elif choice == "2":
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print("Money Deposited Successfully")
        print("New Balance =", balance)
    else:
        print("Invalid Amount")

elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid Amount")

    elif amount > balance:
        print("Insufficient Balance")

    else:
        balance -= amount
        print("Please Collect Your Money")
        print("Remaining Balance =", balance)

elif choice == "4":
    print("Thank you!")

else:
    print("Invalid Choice")
