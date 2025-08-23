# Q4 Write a program to print all odd numbers from 1 to N, where you have to take N as input from user.

num=int(input("Enter a number: "))
for i in range(1,num+1,2):
    print(i, end=" ")
