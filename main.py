print("📚 Student Grade Calculator")

name = input("Enter student name: ")

math = float(input("Math marks: "))
science = float(input("Science marks: "))
english = float(input("English marks: "))
history = float(input("History marks: "))
computer = float(input("Computer marks: "))

total = math + science + english + history + computer
percentage = total / 5

if percentage >= 90:
    grade = "A+ 🌟"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F ❌"

print("\n------ RESULT ------")
print("Student:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
