n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

#nums를 정렬
nums.sort()

group_max = 0
for i in range(n):
    # i번째와 2n-1-i번째 원소를 매칭함, 문제가 원하는 답은 이렇게 해야 나옴
    # num[0]+nums[5], nums[1]+nums[4]
    group_sum = nums[i] + nums[2*n-1-i]
    if group_sum > group_max:
        group_max = group_sum

print(group_max)
