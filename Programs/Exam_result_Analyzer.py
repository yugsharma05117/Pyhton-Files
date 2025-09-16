n= list(input())
m=list(map(int, input().split()))
count_pass=0
count_odd=0
for i in range(len(m)):
    if m[i]<35:
     count_odd+=1
    else:
        count_pass+=1
print(count_pass)
print(count_odd)
