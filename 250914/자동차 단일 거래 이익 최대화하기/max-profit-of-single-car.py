import sys
n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
buy_pr=sys.maxsize
sell_pr=-sys.maxsize

for i in price:
    if i<buy_pr:
        buy_pr=i
    
    loc=price.index(buy_pr)
    
    
    if loc==(n-1):
        break
    
for j in range(loc,n):
    if price[j]>sell_pr:
        sell_pr=price[j]

if loc==(n-1):
    print(0)
else:
    print(sell_pr-buy_pr)