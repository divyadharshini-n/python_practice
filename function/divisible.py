"""Write a Python function that takes a number as input and returns:
Divisible by 5 if the number is divisible by 5
Not divisible by 5 if it’s not divisible by 5"""

def divisible(number):
    if number%5==0:
        return "divisible by 5"
    else:
        return "not divisible by 5"

print(divisible(10))
