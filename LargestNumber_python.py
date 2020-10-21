print('-----Enter three different numbers-----')
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2:"))
n3 = float(input('Enter number 3:'))

if(n1 > n2 and n1 > n3):
    print(n1, " is the largest number")
if(n2 > n1 and n2 > n3):
    print(n2, " is the largest number")
if(n3 > n2 and n3 > n1):
    print(n3, " is the largest number")
