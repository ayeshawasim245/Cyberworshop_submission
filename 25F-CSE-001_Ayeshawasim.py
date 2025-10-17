# Simple Login Form
# Submitted by: Ayeshawasim_25F-CSE-001

# Dummy stored credentials
stored_username = "admin"
stored_password = "12345"

# Ask user for input
print("=== LOGIN FORM ===")
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == stored_username and password == stored_password:
    print("\nLogin Successful!")
else:
    print("\nLogin Failed.")
