import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to B of Password Generator !")

nr_letter = int(input("How many letters you want?\n"))
nr_symbol = int(input("How many symbol you want?\n"))
nr_number = int(input("How many number you want?\n"))

#easy
password = ""

for char in range (1,nr_letter + 1):
  random_char = random.choice(letters)
  password += random_char
for sym in range (1,nr_symbol+1):
  random_sym = random.choice(symbols)
  password += random_sym
for num in range (1,nr_number+1):
  random_num = random.choice(numbers)
  password += random_num

print(password)
