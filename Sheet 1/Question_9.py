# Q9  WAP to check whether a year is a leap year or not.
year= int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("the year is a leap year.")
else:
    print("the year is not a leap year.")