'''
9.Cube of Array
You are provided with an integer array A. Return another array B of size same as that of
A such that B[i] = A[i]^3
Input:
A=[2, 6, 8, 1]
Output:
[8, 216, 512, 1]
'''

a=[2, 6, 8, 1]
b=[]
for i in a:
    b.append(i**3)
print(b)