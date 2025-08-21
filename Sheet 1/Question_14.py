# Q14 Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if num1<num2 and num1<num3:
    print("The minimum element is:", num1)
elif num2<num1 and num2<num3:
    print("The minimum element is:", num2)
elif num3<num1 and num3<num2:
    print("The minimum element is:", num3)
else:
    print("All numbers are equal:", num1, num2, num3)