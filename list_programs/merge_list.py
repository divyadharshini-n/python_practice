a=[1,2,2,2,4,4,5,5]
b=[6,7,8,8,8,9,10]
c=a+b
d=len(c)
counter=0
final_list=[]

for i in range(0,d):
    if c.count(c[counter])>1:
        final_list.append(c[counter])
    counter+=1

e=len(final_list)
f=final_list
print(f)
z=0
y=[]

while z<e:
    if final_list[z] not in final_list:
        y.append(final_list[z])
    z+=1
print(y)














