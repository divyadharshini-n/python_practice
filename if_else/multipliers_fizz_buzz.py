"""
Write a program that prints the numbers from 1 to 100.
But for multiples of 3, print "Fizz" instead, and for multiples of 5 print "Buzz".
For numbers which are multiples of both three and five, print "FizzBuzz".
"""

for i in range (1,101):
    if i%3==0 and i%5==0:
        print("Fizzbus")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)