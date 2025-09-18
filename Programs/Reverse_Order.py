n = int(input())
m = list(map(int, input().split()))

reverse_order = []

for i in range(n):
    if m[i] % 5 == 0:
        reverse_order.append(m[i])

if reverse_order:
    print(*reverse_order[::-1])  
else:
    print(-1)
