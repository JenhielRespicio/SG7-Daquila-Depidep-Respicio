import re

# Ask the user to create a username
username = input("Enter username: ")

# Regex breakdown:
# ^      - Match the start of the string
# [a-zA-Z0-9] - Allow only uppercase letters, lowercase letters, and numbers
# {5,10} - Ensure the length is between 5 and 10 characters inclusive
# $      - Match the end of the string
if re.match(r"^[a-zA-Z0-9]{5,10}$", username):
    print("Valid username.")
else:
    print("Invalid username.")
