n = int(input())
m=list(map(int,input().split()))
count_days=0
for i in range(1,n):
    if m[i]<m[i-1]:
        count_days+=1
print(count_days)