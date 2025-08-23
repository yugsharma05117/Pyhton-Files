# Q6 You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A.

num= int(input("Enter a integer A: "))
sum=0
for i in range(2,num+1,2):
    sum=sum+i
print("The sum of all even numbers from 1 to", num, "is", sum)