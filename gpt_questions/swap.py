"""Ask the user to enter two numbers.
Swap their values without using a third variable.
Print the numbers before and after swapping"""

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print("before swapping:",a,b)
a=a+b
b=a-b
a=a-b
print("after swapping:",a,b)


