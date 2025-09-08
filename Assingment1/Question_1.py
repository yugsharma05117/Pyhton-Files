'''Ques 1:
n = 5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

n= int(input())
for i in range(1,n):
    for j in range(n):
        print("*", end=" ")
    print()
