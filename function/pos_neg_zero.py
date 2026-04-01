"""Write a Python function that takes a number and returns whether the number is:
Positive if it’s greater than 0
Negative if it’s less than 0
Zero if it is 0"""

def check_number(a):
    if a>0:
        return "positive"
    elif a<0:
        return "negative"
    else:
        return "zero"
print(check_number(2))


