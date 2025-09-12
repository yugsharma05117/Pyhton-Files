'''
2.Copy the Array
You are given a constant array A and an integer B.
You are required to return another array where Arr[i] = A[i] + B.
Input :-
A = [1 2 3 2 1]
B = 3
Output:
[4 5 6 5 4]
'''

arr=[1, 2, 3, 2, 1]
b=3
new_arr=[]
for i in arr:
    new_arr.append(i+b) 
print(new_arr)