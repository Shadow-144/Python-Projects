# importing some modules for the project 
import random
import time

opera = ["+", "-", "*"] 
min_val = 3
max_val = 9
total_question = 5

def generate_question():
    left = random.randint(min_val, max_val)
    right = random.randint(min_val, max_val)
    a = random.choice(opera)
    question = str(left) + " " + a + " " + str(right)
    answer = eval(question)
    return question, answer

input("Press Enter to start ")
print("---------------------")

start_time = time.time()

for i in range(1, total_question+1): 
    question , answer = generate_question()
    while True: 
        guess = input(("Problem #") + str(i) + ": " + question + " = ")
        if(guess == str(answer)): 
            break 
        else: 
            print("Try again!")
  
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------")
print("You finished in" ,total_time)