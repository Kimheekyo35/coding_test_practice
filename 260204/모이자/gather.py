n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_sum = 1000000000000

for i in range(n):
    diff_sum = 0
    point = A[i]

    for j in range(n):
        diff_sum += abs(j-i)*A[j]

    min_sum = min(min_sum,diff_sum)
print(min_sum)