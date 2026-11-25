import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

while True:
    length = int(input("How many characters should your password have? "))

    if length > 0:
        break

    print("Please enter a positive number.")

password = ""

for i in range(length):
    password += random.choice(all_characters)

print(f"Your generated password is: {password}")