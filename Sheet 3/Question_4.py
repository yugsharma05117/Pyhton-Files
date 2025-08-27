#1
#1 *
#1 * 3
#1 * 3 *
#1 * 3 * 5
#print the following pattern
for i in range(1,6,2):
    for j in range(1,i+1,2):
        print(j, end="* ")
    print()
    