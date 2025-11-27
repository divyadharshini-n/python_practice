"""Takes marks of 3 subjects as input.
If the average ≥ 40 → print "Pass".
Otherwise → print "Fail".
Bonus: Also print the average score."""

maths = int(input("Enter the mark 1:"))
science = int(input("Enter the mark 2:"))
social = int(input("Enter the mark 3:"))
average = (maths+science+social)/3
print(average)
if average >= 40:
    print("Pass")
else:
    print("Fail")