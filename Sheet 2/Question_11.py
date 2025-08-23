# Q11 Take a number A as input, print its multiplication table having the first 10 multiples.

number= int(input("Enter a number for table:"))
for i in range(1,11):
    print(number,"X",i,"=",number*i)