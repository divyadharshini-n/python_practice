a = int(input("1:Toys , 2:Books and 3:furniture :"))

if a==1:
    item_lists={
        "car":10,
        "bear":20,
        "rabit":30,
        "goat":40,
        "cat":50
    }
elif a==2:
    item_lists={
        "harry":100,
        "potter":200,
        "python":300,
        "java":400,
        "oops":500
    }
elif a==3:
    item_lists={
        "chair":120,
        "table":200,
        "bed":300,
        "sofa":400,
        "tea table":400
    }
else:
    print("invalid choice")

price=0
total=0

while True:
    print(item_lists)
    items=input("enter the item :").split()
    quantity=int(input("enter the quantity :"))

    for item in items:
        if item in item_lists:
            price = item_lists[item]*quantity
            print("total cost:",price)
            total += price
        else:
            print("items are not available")

    more=input("want to buy more?")
    if more!="yes":
        break

