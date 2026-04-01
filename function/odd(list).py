#odd numbers from a list

def odd_num(numbers):
    count=[]
    for num in numbers:
        if num%2!=0:
            count.append(num)
    return count
print("the odd numbers are",odd_num([1,2,3,4]))


