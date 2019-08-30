n = int(input("enter the no.  : "))
rem = 0
product = 1
while(n != 0):
    rem = n % 10
    product = product * rem
    n = n // 10
print(product)
