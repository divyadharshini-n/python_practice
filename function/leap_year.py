#leap year
def leap_year(year):
    if year%400==0:
        return "leap year"
    else:
        return "not a leap year"
print(leap_year(1999))