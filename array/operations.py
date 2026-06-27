from array import array

#ACCESSING
arr=array("i",[1,2,3,4,5])
print("The Zeroth index element is:",arr[0])

#INSERT
arr.insert(0,11)
print(arr)

#DELETE BY INDEX
arr.pop(0)
print(arr)

#SEARCHING
for j in range(0,len(arr)):
    if arr[j]==3:
        print(j)

search=int(input("Enter the element to search:"))
for i in range(0,len(arr)):
    if arr[i]==search:
        print(i)
        break
    else:
        print("Element not found")
        break







