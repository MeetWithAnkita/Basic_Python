# Predefined users and passwords
users = {"admin": "1234", "user": "abcd", "guest": "guest"}

username = input("Enter username: ").strip()
if username not in users:
    print("Invalid username.")
else:
    password = input("Enter password: ").strip()
    if users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password.")