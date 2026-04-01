"""Write a Python function that:
Takes a number n as input
Returns the sum of numbers from 1 to n
Use a loop (for or while) inside the function
Print the result directly without storing"""

def input_num(number):
    count=0
    for i in range(1,number):
        count+=i
    return count
print("the sum is",input_num(10))



