# Taking input from the user 
name = input("Enter your name : ")
print(f"Welcome to the game of your dreams , {name}")
# The adventure of dreams of the user
q_1 = input("You have been teleported to a new world and you have two ways right or left Which way you wanna go (right/left): ").lower()
if(q_1 ==  "right"): 
    q_2 = input("you have reached a river do you wanna cross it throught the brige or swim across (cross/swim): ").lower()
    if(q_2 == "cross"):
        q_3 = input("You have reached to a palace do you wanna go inside the palace or not (Yes/No): ").lower()
        if(q_3 == "yes"): 
            q_4 = input("You have seen a beautiful girl do you want to ask her name (Yes/No): ").lower()
            if(q_4 == "yes"): 
                print("you woke up and it was a dream")
            elif(q_4 == "no"):
                print("Game over")
            else: 
                print("Not a valid option")
        elif(q_3 == "no"): 
            print("Game over")
        else: 
            print("Not a valid option")
    elif(q_2 == "swim"): 
        print("Ops there was a crocodile you have been eaten by it")
    else: 
        print("Not a valid option")
elif(q_1 == "left"): 
    print("There was a Dragon and you were eaten by the dragon : ")
else: 
    print("Not a valid option")