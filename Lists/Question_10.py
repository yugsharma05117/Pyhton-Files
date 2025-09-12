'''
10.Reverse
Given an array A, Find the reverse of it. (Solve this question with for loop)
Input:
A = [3, 5, 1, 2, 1, 2]
Output:
[2, 1, 2, 1, 5, 3]
'''
A = [3, 5, 1, 2, 1, 2]
n = len(A)
rev = []
for i in range(n-1, -1, -1):
    rev.append(A[i])
print(rev)