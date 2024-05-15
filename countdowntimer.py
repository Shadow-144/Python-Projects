#importing time module 
import time 
# definig a function for timer
def countdown(t):
    while t: 
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer)
        time.sleep(1)
        t-=1
    print("The Timer has ended")
# Taking input from the user
t = input("Enter the time in seconds : ")
countdown(int(t))