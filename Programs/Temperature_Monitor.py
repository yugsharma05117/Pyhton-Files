n= int(input())
m=list(map(int,input().split()))
average=0
for i in range(0,n):
    if m[i]>40:
        average+=1
print(average)