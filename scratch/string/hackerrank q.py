arr = []
arr.append(6)
arr.append(5)
arr.append(10)
print(arr)

arr.remove(6)
#arr.append(1)
#arr.append(9)
arr.extend([1,9])
arr.sort()
print(arr)

arr.remove(10)
arr.reverse()
print(arr)
