# Date: 15 July 2025
# Title: Random Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("This is a password Generator using Python")

#user input
ps_letters = int(input("How many letters would you like in your password?\n"))
ps_sysmbols = int(input(f"How many symbols would you like?\n"))
ps_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
#password = ""
#for char in range(0, ps_letters):
#    password += random.choice(letters)
#
#for char in range(0, ps_sysmbols):
#    password += random.choice(symbols)
#
#for char in range(0, ps_numbers):
#    password += random.choice(numbers)
#
#print(password)

#hard level

password_list = []
for char in range(0, ps_letters):
    password_list.append(random.choice(letters))

for char in range(0, ps_numbers):
    password_list.append(random.choice(symbols))

for char in range(0, ps_sysmbols):
    password_list.append(random.choice(symbols))

print(password_list)

#to shuffle the list
random.shuffle(password_list)
print(password_list)

#to combine the string for password
#password = ''.join(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")