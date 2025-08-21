# Q13 Write a program to input two numbers(A & B) from the user and print the maximum element among A & B.
A = int(input("Enter first number A: "))
B = int(input("Enter second number B: "))
if A > B:
    print("The maximum element is:", A)
elif B > A:
    print("The maximum element is:", B)
else:
    print("Both numbers are equal:", A)