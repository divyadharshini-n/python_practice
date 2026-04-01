"""Takes marks for 3 subjects.
The student passes only if all subjects ≥ 40.
If any subject is below 40 → print "Fail".
Otherwise → print "Pass"."""

tamil = int(input("Enter the marks 1:"))
english = int(input("Enter the marks 2:"))
maths = int(input("Enter the marks 3:"))
average = (tamil+english+maths)/3
print ("Average",average)
if tamil>=40 and english >= 40 and maths>= 40 :
    print ("pass")
else:
    print("Fail")

