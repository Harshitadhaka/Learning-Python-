num = int("input("Enter a number:"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit 
    num = num // 10

print("Reversed Number =", reverse)

num = int(input("Enter a Number: "))

reverse = 0

while num > 0:
   digit = num % 10
   reverse = reverse * num + digit 
   num = num // 10

print("Received Number =", reverse)
