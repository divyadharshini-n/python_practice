#Return List of Squares


def square(number):
    count=[]
    for num in number:
        count.append(num*num)
    return count
print("the square of numbers ina list are",square([1,2,3]))
