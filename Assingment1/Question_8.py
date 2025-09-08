'''
Ques 8:
n = 5
* *
* *
*
* *
* *
'''

n=5
for i in range(n):
    if i==0 or i==n-1 or i!=n//2:
        print("* "*2)
    else:
        print("*")