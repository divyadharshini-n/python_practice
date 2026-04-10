import random
num = random.randint(0,20)
user = ''
while num != user:
    user = int(input("Enter the number:"))
    if user > num:
        print("Your guess is higher")
    else:
        print("your guess is lower")
        user = int(input("Enter the number:"))


print("WINNER!")