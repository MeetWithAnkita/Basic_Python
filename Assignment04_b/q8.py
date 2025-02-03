# Prompt the user to enter the number of email addresses
email_count = int(input("Enter the number of email addresses: "))

# Initialize counters
student_count = 0
professor_count = 0

# Process each email
for _ in range(email_count):
    email = input("Enter an email address: ")
    if email.endswith("@student.tiu.edu"):
        student_count += 1
    elif email.endswith("@prof.tiu.edu"):
        professor_count += 1

# Print the results
print(f"\nNumber of student email addresses: {student_count}")
print(f"Number of professor email addresses: {professor_count}")