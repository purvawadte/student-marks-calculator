# Student Marks Calculator
# Author: Purva
# Description: Calculates total, percentage and grade

# Taking input
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

# Calculating total
total = m1 + m2 + m3 + m4 + m5

# Calculating percentage
percentage = total / 5

# Grade logic
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Output
print("\n----- RESULT -----")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

# Pass/Fail status
if percentage >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")