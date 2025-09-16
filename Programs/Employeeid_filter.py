

n=int(input())
m=list(map(int,input().split()))
even=[]
for i in range(len(m)):
    if m[i]%2==0:
        even.append(m[i])
if even:
    print(even)
else:
    print(-1)


