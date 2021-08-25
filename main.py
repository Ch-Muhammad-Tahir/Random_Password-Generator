#   PyPassword Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numberS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','@','?']
print("Welcome To PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
# password = ""
# for char in range(1, nr_letters+1):
#     random_char = random.choice(letters)
#     password += random_char
#
# for char in range(1, nr_symbols+1):
#     random_char = random.choice(symbols)
#     password += random_char
#
# for char in range(1, nr_numbers+1):
#     random_char = random.choice(numberS)
#     password += random_char
# print(password)

# Hard Level

password_list = []
for char in range(1, nr_letters+1):
    # You can Also Use Append function instead of
    # password_list += random.choice(letters)
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers+1):
    password_list += random.choice(numberS)

# Print Password List before  Shuffle
#print(password_list)

random.shuffle(password_list)

# Print Password List After  Shuffle
#print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your Password is :{password}")