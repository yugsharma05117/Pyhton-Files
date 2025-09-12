'''
11. Add two list element:
Given two lists A1 and A2, each containing integers, write a Python program to compute
the element-wise sum of the corresponding elements in the two lists and store the result
in a new list.
Input:
A1=[1, 2, 3,4]
A2=[4, 5, 6,7]
Output:
[5, 7, 9, 11]
'''
a1=[1, 2, 3,4]
a2=[4, 5, 6,7]
result=[]
for i in range(len(a1)):
    result.append(a1[i]+a2[i])
print(result)
