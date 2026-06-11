# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Input-Output Exercise #1
# DATE WRITTEN: 8/26/2020
#
# PURPOSE: Demonstrate use of string literal and variable objects
#          implemented using input/output operations.
#          Collects student information and displays it in a formatted report.
#
# VARIABLES (alphabetical):
#   collegeMajor  - stores the student's college major
#   semester      - stores the current semester the student is attending
#   studentName   - stores the student's full name

# Initialize variables to empty strings to ensure accuracy of stored data
collegeMajor = ""
semester = ""
studentName = ""

# INPUT OPERATIONS
print("Please enter the student's full name: ")
studentName = input().strip()

print("What is " + studentName + "'s college major? ")
collegeMajor = input().strip()

print("Enter the current semester attending for " + studentName + ": ")
semester = input().strip()

# OUTPUT OPERATIONS
print()
print("================================================================")
print("INFORMATION FOR: " + studentName)
print("MAJOR: " + collegeMajor)
print("CURRENT SEMESTER ATTENDING: " + semester)
print("================================================================")

# END PROGRAM
