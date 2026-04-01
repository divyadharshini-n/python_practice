
c=int(input("Enter 1 or 2:"))

def number():
    array=[]
    for a in range(5):
        a = int(input("enter the number :"))
        array.append(a)
    print(array)
def mul_10():
    aray = []
    for b in range(5):
        b = int(input("enter the number :"))
        b=b*10
        aray.append(b)
    print(aray)

if c==1:
    number()
elif c==2:
    mul_10()
else:
    print("Invalid input")



