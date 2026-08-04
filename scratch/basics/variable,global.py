#method 1
x = "fruits"
print(x)

#method 2
a,b = "cats","dogs" #num of variables = num of values
print(a)
print(b)
print(a,b)

#method 4
var1 = var2 = var3 = "monkey"
print(var1)

#method 5
var4="pok"
var5="cut"
print(var4,var5)

#Global Variable and GLOBAL keyword
color = "Black"
def rainbow ():
    print("I love",color)
rainbow()

#To change the global variable inside a function, use global keyword
veg = "Carrot"
def veggies():
    global veg
    veg = "Beans"
veggies()
print(veg)

