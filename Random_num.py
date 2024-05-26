import random
#using the random module to create a number guessing game for the user 
random_num = random.randint(1 , 50)
guess = 0
while guess != random_num:
    guess = int(input("Enter your gussed number from 1 to 50 : "))
    if random_num > guess:
        print("you are too low")
    elif(random_num < guess):
        print("you are too high")

print("Congratulations you guessed your number")

