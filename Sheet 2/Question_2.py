# Q2 Write a program to print all Natural numbers from N to 1, where you have to take N as input from the user.
num= int(input("Enter a positive integer:"))
for i in range(num, 0, -1):
    print(i, end=" ")