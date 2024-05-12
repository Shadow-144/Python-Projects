#Taking input from the user and printing the vowels in it

str = input("Enter the string : ")
b = str.lower()
for i in range(len(str)):
    a = b[i]
    if (a == "a") or (a == "e") or (a == "i") or (a == "o") or (a == "u"):
        print (a)