#Write a progam that multiplies two integer number without using the * operator, using repeated addition
n1= int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
product=0
count=n1
while count>0:
    count=count-1
    product=product+n2
print("The product of",n1,"and",n2,"is",product)
