def largest(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("First Number: "))
y = int(input("Second Number: "))

print("Largest =", largest(x, y))
