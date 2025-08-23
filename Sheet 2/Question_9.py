# Q9 Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.

num= int(input("Enter an integere N: "))
sum= 0
for i in str(num):
    sum= sum+ int(i)
print("The sum of digits in the number", num, "is", sum)
