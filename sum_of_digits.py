n = int(input("enter the the no.  : "))
d = 0; sum = 0
while (n != 0):
    d = n % 10
    sum = sum + d
    n = n//10
print(sum)

