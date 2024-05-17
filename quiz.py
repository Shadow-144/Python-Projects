# Greeting the user
print("Welcome to our Quiz Game!")
# Keeping Track of score of the user
score = 0
# Player wants to play
print("Okay! ok Let's play")
# Questions  for the game
answer = input("What does RAM stands for? ")
if(answer.lower() == "random access memory"):
    print("Correct answer!")
    score += 1
else: 
    print("Incorrect answer")

answer = input("Who invented Compact Disc? ")
if(answer.lower() == "james t. russell"):
    print("Correct answer!")
    score += 1
else: 
    print("Incorrect answer")

answer = input("In the virtual world, WWW stands for ___________________________. ")
if(answer.lower() == "world wide web"):
    print("Correct answer!")
    score += 1
else: 
    print("Incorrect answer")

answer = input("What is also known as a portable computer? ")
if(answer.lower() == "laptop"):
    print("Correct answer!")
    score += 1
else: 
    print("Incorrect answer")

answer = input("Name the device that is used to take a printout of a document from a computer. ")
if(answer.lower() == "printer"):
    print("Correct answer!")
    score += 1
else: 
    print("Incorrect answer")

print(f"You got {score} out of 5!")
percent = (score/5)*100
print(f"You got {percent}" + "%")