from random import random, choice, randint, shuffle

upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_upper_letters = int(input("How many upper-case letters would you like in your password?\n"))
n_lower_letters = int(input("How many lower-case letters would you like in your password?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

total_string_sum = n_upper_letters + n_lower_letters + n_symbols + n_numbers
selected_upper_letters = []
selected_lower_letters = []
selected_numbers = []
selected_symbols = []
final_password_list = []
#getting required upper case letters
for i in range(0, n_upper_letters):
    selected_upper_letters += choice(upper_letters)
#getting required lower case letters
for i in range(0, n_lower_letters):
    selected_lower_letters += choice(lower_letters)
#getting required numbers
for i in range(0, n_numbers):
    selected_numbers += choice(numbers)
#getting required symbols
for i in range(0, n_symbols):
    selected_symbols += choice(symbols)
final_password_list = selected_upper_letters + selected_lower_letters + selected_numbers + selected_symbols
shuffle(final_password_list)
final_password = ""
#place selected strings in random position
for i in range(0, total_string_sum):
    final_password += final_password_list[i]
print(f"\nYour final password is {final_password}\nYour password contains {total_string_sum} digits.\n")