'''
Ques 11:
n = 5
*
* *
* * *
* * * *
* * * * *
'''
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()