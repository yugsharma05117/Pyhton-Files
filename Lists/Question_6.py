'''
6.Even Odd Elements
For array A, you have to find the value of absolute difference between the counts of
even and odd elements in the array.
Input:
A = [1 2 3 4]
Output:
0
'''
a=[1, 2, 3, 4]
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
result=even-odd
print(result)