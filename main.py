print("📚 Student Grade Calculator")
print("-" * 30)

name = input("Enter student name: ")

subjects = {
    "Math": float(input("Math marks: ")),
    "Science": float(input("Science marks: ")),
    "English": float(input("English marks: ")),
    "History": float(input("History marks: ")),
    "Computer": float(input("Computer marks: "))
}

total = sum(subjects.values())
percentage = total / len(subjects)

# Grade
if percentage >= 90:
    grade = "A+ 🌟"
elif percentage >= 80:
    grade = "A 🥇"
elif percentage >= 70:
    grade = "B 👍"
elif percentage >= 60:
    grade = "C 🙂"
elif percentage >= 50:
    grade = "D 😐"
else:
    grade = "F ❌"

# Pass or Fail
status = "PASS ✅" if percentage >= 40 else "FAIL ❌"

# Highest scoring subject
highest_subject = max(subjects, key=subjects.get)

print("\n🎓 RESULT")
print("-" * 30)
print("Student:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
print("Status:", status)
print("Best Subject:", highest_subject, "-", subjects[highest_subject])
