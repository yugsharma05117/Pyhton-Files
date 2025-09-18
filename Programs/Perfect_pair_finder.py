n= int(input())
m=list(map(int, input().split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if m[i]+m[j]==n:
            count+=1
print("Number of pairs are:", count)
        