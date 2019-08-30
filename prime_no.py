n = int(input("enter the no.  : "))
c =0
for i in range(1,n//2,1):
    if n % i ==0 :
        c = c+1
if (c > 2):
    print("this is not a prime ")
else:
    print("This is  a prime no ")