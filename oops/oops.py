import json

choice = input("Do you want to add or want to bill?:").lower()

def adder ():
    i=0
    add_count = int(input("How many items do you want to add?:"))
    for i in range (0,add_count):
        add_item = input("Enter the item:").lower()
        price = int(input("Enter the price of " + add_item + ":"))
        i+=1
        store = {"item":add_item,"price":price}
        with open("item.jsonl","a") as file:
            file.write(json.dumps(store)+"\n")
        print(store)

def biller ():
    bill_item = input("Enter the item to bill:").lower()
    found = False

    with open("item.jsonl", "r") as file:
        for line in file:
            data = json.loads(line)

            if data["item"] == bill_item:
                print("The price of", bill_item, "is", data["price"])

                quantity = int(input("Enter quantity: "))
                total_price = data["price"] * quantity
                print("Total price is:", total_price)

                found=True
                break
    if not found:
            print("Item not available")


if choice == "add":
     adder()
elif choice == "bill":
    biller()
else:
    print("Invalid input")
