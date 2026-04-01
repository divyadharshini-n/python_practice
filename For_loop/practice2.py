
num_list = []
while True:
    num = input("Enter the number of list, enter 'z' to exit:")
    if num == "z":
        break
    else:
        num=int(num)
        num_list.append(num)
print(num_list)
