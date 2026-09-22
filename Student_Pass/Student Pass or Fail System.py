name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

if maths >= 33 and physics >= 33 and chemistry >= 33:
    print(name, "has Passed")

    total = maths + physics + chemistry
    percentage = total / 3

    print("Percentage =", percentage)

else:
    print(name, "has Failed")
