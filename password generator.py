import random

# Define character sets
letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters_upper = [letter.upper() for letter in letters_lower]  # Uppercase letters
symbols = ["!", "@", "#", "$", "%", "&", "*"]  # Essential symbols
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# User input
num_letters = int(input("How many letters do you want? "))
num_symbols = int(input("How many symbols do you want? "))
num_numbers = int(input("How many numbers do you want? "))

# Generate password components
password = []

# Add letters (randomly mix lowercase and uppercase)
for _ in range(num_letters):
    random_letter = random.choice(letters_lower + letters_upper)
    password.append(random_letter)

# Add symbols
for _ in range(num_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

# Add numbers
for _ in range(num_numbers):
    random_num = random.choice(numbers)
    password.append(random_num)




# Convert list to string
final_password = "".join(password)

# Output the generated password
print(f"Your password is: {final_password}")
