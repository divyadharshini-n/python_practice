"""
get the numbers as user input.
run the program until the user enters stop.
store them in a list.
search the number in which the user enters.
find index of the number in which the user enters.
get sum,maximum,minimum,average.
remove,reverse,sort.
"""

#get the numbers as user input.
store_numbers=[]
while True:
    number = input("enter the number(or stop):")
    if number == "stop":
        break
    if number.isdigit():
        numbers=int(number)
        store_numbers.append(numbers)
print("the numbers are",store_numbers)


#search the number in which the user enters.
find = int(input("enter the number to search:"))
if find in store_numbers:
    print("number found")
else:
    print("number not found")

#find index of the number in which the user enters.
find_index = int(input("enter the index to search:"))
if find_index in store_numbers:
    print("the index of",find_index,"is",store_numbers.index(find_index))
else:
    print("index not found")

#even numbers

#length
length = len(store_numbers)
print("the lenght of the list is:",length)

#sum
summ = sum(store_numbers)
print("the sum of list is:",summ)

#max,min,average
print("maximum of list is:",max(store_numbers))
print("minimum of list is:",min(store_numbers))
print("the average of the list is:",summ/length)

#remove
remove_number = int(input("enter the number to remove:"))
if remove_number in store_numbers:
    store_numbers.remove(remove_number)
    print("numbers after removed:",remove_number)
else:
    print(store_numbers)

#reverse
store_numbers.reverse()
print("the reversed list is:",store_numbers)

#sort
store_numbers.sort()
print("the sorted list is:",store_numbers)













