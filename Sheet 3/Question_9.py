#Print the following pattern
'''
**********
**** ****
***   ***
**     **
*       *
'''

n=int(input("Enter the number: "))
for i in range(1, n+1):
    for j in range(n+1-i):
        print("*", end="")
    for j in range(2*(i-1)):
        print(" ", end="")
    for j in range(n+1-i):
        print("*", end="")
    print()