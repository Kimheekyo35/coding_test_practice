m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

year_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]

day_sum = 0
for i in range(m1,m2):
    if i == m1:
        day_sum += (year_list[i] - d1) + 1
    else:
        day_sum += year_list[i]
day_sum += d2

print(day_sum)