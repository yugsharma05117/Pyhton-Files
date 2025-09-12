'''
8.Square of Array
You are provided with an integer array A. Return another array B of size same as that of
A such that B[i] = A[i]^2
Input:
A=[2, 6, 8, 1]
Output:
[4, 36, 64, 1]
'''

a=[2, 6, 8, 1]
b=[]
for i in a:
    b.append(i**2)
print(b)