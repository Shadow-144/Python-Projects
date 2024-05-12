import random
# Creating a rock paper and scissor game
# computer choosing 
l = ["Rock" , "Paper", "Scissor"]
com = random.choice(l)

# usr choosing 
usr = input("Choose \'Rock , Paper , Scissor\' : ")
print("The computer choose : ", com)
a = usr.capitalize()

# condition 
if(a == com):
    print("It is a draw")
elif(a == "Rock" and com == "Scissor") or (a == "Scissor" and com == "Paper") or (a == "Paper" and com == "Rock"):
    print("The user wins") 
else: 
    print("The Computer Wins")