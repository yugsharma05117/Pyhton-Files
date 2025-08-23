# Q5 Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from use

num= int(input("Enter a number: "))
sum= 0
for i in range(1,num+1):
    sum= sum+i
print("The sum of all natural numbers from 1 to", num, "is", sum)