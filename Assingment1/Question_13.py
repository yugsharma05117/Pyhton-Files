'''
Ques 13:
n = 5
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i-1):
        print("*",end=" ")
    print()