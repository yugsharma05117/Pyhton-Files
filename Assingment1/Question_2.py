'''
Ques 2:
n = 5
*
* *
* * *
* * * *
* * * * *
'''

n= int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()

