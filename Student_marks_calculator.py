name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 3

print("\n===== RESULT =====")
print("Student:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")

elif percentage >= 80:
    print("Grade: B")

elif percentage >= 70:
    print("Grade: C")

elif percentage >= 60:
    print("Grade: D")

else:
    print("Grade: F")
