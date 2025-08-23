# Q8 Take an integer N as input and print the count of digits of that number
num=int(input("Enter an integer N: "))
count= 0
for i in str(num):
    count=count+1
print("The count of digits in the number", num, "is", len(str(num)))