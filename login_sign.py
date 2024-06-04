# Logic for signing up
def sign_up():
    with open("sign.txt", "a") as s:
        s.write(account_name + "|" + password + "\n")
# logic for login
def login():
    with open("sign.txt", "r") as s:
            K = False
            for line in s.readlines():
                data = line.rstrip()
                user, passwd = data.split("|")
                if(account_name == user) and (password == passwd):
                    print("Login successful!")      
                    K = True
            if(not K):
                print("Invalid Username or Password")
# Tell sign up or login
choose = int(input("Would you like to login or sign up (1 = login/ 2 = signup): "))
# Taking the user name and password to store or login
if(choose == 1):
    account_name = input("account_name : ").lower() 
    password = input("password name : ").lower()
    login()
else:
    account_name = input("account_name : ").lower() 
    password = input("password name : ").lower()
    sign_up()