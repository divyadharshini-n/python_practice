num = [2,2,4,5,6,7,7,8,9,9,11,11]
b=0
while b<len(num):
    if num.count(num[b]) > 1:
        num.pop(b)
    else:
        b+=1
print(num)
