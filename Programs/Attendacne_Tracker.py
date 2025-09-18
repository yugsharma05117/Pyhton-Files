n=int(input())
m=list(map(int, input().split()))
attendance=0
for i in range(len(m)):
    if m[i]==1:
        attendance+=1
print("No. of attendes:", attendance)