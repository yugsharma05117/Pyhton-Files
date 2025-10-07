n = int(input()) 
eligible = 0

for i in range(n):
    data=input().split()
    marks=int(data[0])
    attendance=int(data[0])
    #marks, attendance = map(int, input().split())
    if marks >= 75 and attendance >= 80:
        eligible += 1

print(eligible)
