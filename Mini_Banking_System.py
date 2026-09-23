balance = 1000

while True:

    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance =", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            balance += amount
            print("Deposit Successful")
            print("New Balance =", balance)
        else:
            print("Invalid Amount")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid Amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:
            balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance =", balance)

    elif choice == "4":
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid Choice")
