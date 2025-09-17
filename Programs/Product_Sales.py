#A store keeps a list of sales of n products. Each product has a sales count. The manager wants
#to print the highest-selling product count and the lowest-selling product count.

n=int(input())
m=list(map(int, input().split()))
print("highest selling product count is: ",max(m))
print("minimum selling product count is :", min(m))