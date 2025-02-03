contacts = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'},
]

# a) Phone ending with 8
phone_eight = [person['name'] for person in contacts if person['phone'].endswith('8')]

# b) Missing email
missing_email = [person['name'] for person in contacts if not person['email']]

print("Phone ending with 8:", phone_eight)
print("Missing email:", missing_email)