# Q10 You are given an integer A as input, and you need to determine whether it is a palindrome or not from for method.

num=int(input("Enter a number: "))
if str(num)==str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")