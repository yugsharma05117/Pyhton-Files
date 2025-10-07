# WAP that inputs an integer in range 0-999 and then prints if the entered integer is a 1/2/3 digit number. Use nested if
num= int(input("Enter the integer: "))
if num<0 or num>999:
    print("Invalid Entry")
else:
    if num<10:
        print("The integer entered is a 1 digit number")
    else:
        if num<100:
            print("The integer entered is a 2 digit number")
        else:
            print("The integer enetered is a 3 digit number")
            
