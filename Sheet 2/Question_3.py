# Q3 Write a program to print all even numbers from 1 to N, where you have to take N as input from the user.
num= int(input("Enter a positive integer: "))
for i in range(2, num+1, 2):
    print(i, end=" ")