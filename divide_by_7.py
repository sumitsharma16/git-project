a = int(input("enter the 1st no. of range  :  "))
b = int(input("enter the 2nd no. of range  :  "))
c = 0
for i in range (a,b,1):
    if i%7  == 0:
        c+=1
print(c)
