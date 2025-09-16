import sys
n = int(input())
price = list(map(int, input().split()))

max_profit=0
for i in range(n):
    for j in range(i,n):
        if price[j]-price[i]>max_profit:
            max_profit=price[j]-price[i]

print(max_profit)