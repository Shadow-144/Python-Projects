# empty list 
LA = []
LB = []
LC = []
# Taking input from the user  & storing it
for i in range(1 ,6,1):
    std = input("Enter the name : ")
    roll = int(input("Enter the Roll no. : "))
    mark = int(input("Enter the marks : "))
    if(mark>=80):
        print("The student is in Group A")
        LA.append(mark)
    elif(mark>=70):
        print("The student is in Group B")
        LB.append(mark)
    else:
        print("The student is in Group C")
        LC.append(mark)
# Calculating the sum of indiviual groups 
a = sum(LA)
b = sum(LB)
c = sum(LC)
# Calculating the avg of indiviual groups 
A = a/len(LA)
B = b/len(LB)
C = c/len(LC) 
# Printing the avg of each group
print("The average of Group A is ", A)
print("The average of Group B is ", B)
print("The average of Group C is ", C)
