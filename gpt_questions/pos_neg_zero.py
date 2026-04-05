"""Takes a number as input.
Checks whether the number is positive, negative, or zero.
Prints the result"""

a = int(input("Enter the number:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")