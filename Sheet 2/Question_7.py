# Q7 . Take an integer A as input. You have to print the sum of all odd numbers in the range [1,A].

num= int(input("ENter a integer A: "))
sum=0
for i in range(1,num+1,2):
    sum= sum+i
print("The sum of all odd numbers from 1 to", num, "is", sum)