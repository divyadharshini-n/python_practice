"""Ask the user for a number n.
Print the sum of all numbers from 1 to n."""

n = int(input("Enter the number:"))
total = 0
for i in range (1,n+1):
    total+=i
print("sum:",total)


