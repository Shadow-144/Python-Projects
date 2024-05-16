# importing random module 
import random
# making random string to generate passwd
ran = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-/|<>.,"
# Taking user input 
num_of_pass = int(input("Enter the number of password you want to create : "))
length = int(input("Enter the length of your passwords : "))
# logic for the password
for passwd in range(num_of_pass):
    passwds = ""
    for c in range(length):
        passwds = passwds + random.choice(ran)
    print(passwds)