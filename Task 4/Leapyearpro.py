# Create a program that checks if a given year is a leap year.

year = int(input("Enter a Year:"));

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True;
    else:
        return False;

if leap_year(year):
    print({year},"is leap year");
else:
    print({year},"is not leap year");
