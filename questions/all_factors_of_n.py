#Get input number n from user. Print all the factors of n.

n = int(input("enter the number:"))
for i in range (1,n+1):
    if n % i == 0:
        print(i)

