n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_num = 0
for i in range(n-1):
    for j in range(i+2,n):
        total = numbers[i] + numbers[j]
        max_num = max(total,max_num)

print(max_num)
        
