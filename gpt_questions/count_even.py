"""Takes a number n
Counts how many even numbers exist from 1 to n
Prints the count"""

n = int(input("Enter the number:"))
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print("Even numbers from 1 to n:",count)