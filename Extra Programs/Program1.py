#Write a program that inputs an integer in range 0-999 and then prints if the integer enetered is 1/2/3 digit number
num=int(input("Enter the number: "))
if num<10:
    print("Invalid Entry")
elif num<100:
    print("Two digit entry")
elif num<=999:
    print("Three digit entry")
else:
    print("Invalid Entry")
