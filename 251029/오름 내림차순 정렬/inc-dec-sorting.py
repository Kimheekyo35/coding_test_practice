n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# nums_up = sorted(nu)
# print(*nums_up)
# nums_down = list(reversed(nums_up))
# print(*nums_down)

# sort는 original 값을 바꿈
# sorted는 original 값 변경 안함
nums.sort()
print(*nums)
nums.sort(reverse=True)
print(*nums)