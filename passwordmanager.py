# fuction to view the password
def view(): 
      with open("password.txt", "r") as f: 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user , "| Password:", passw)
# fuction to add the password       
def add():
    account_name = input("Enter the account name : ")
    password = input("Enter the password for the accout : ")
    with open("password.txt", "a") as f: 
        f.write(account_name + "|" + password + "\n")
#input from the user 
while True:
    mode = input("Would you like to view or add a password ? (view/add) or Enter q to quit: ").lower()
    if(mode == "q") : 
        break
    elif(mode == "view"):
        view()
    elif(mode == "add"): 
        add()
    else: 
        print("Invalid option")
