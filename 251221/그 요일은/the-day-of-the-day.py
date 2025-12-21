m1,d1,m2,d2 = tuple(map(int,input().split()))
a = input()

day_name = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
monthly_day = [0,31,29,31,30,31,30,31,31,30,31,30,31]


def count_day(month,day):
    total_day = 0
    for i in range(1,month):
        total_day += monthly_day[i]
    total_day += day
    
    return total_day

m1d1_cnt = count_day(m1,d1)
m2d2_cnt = count_day(m2,d2)

diff = m2d2_cnt - m1d1_cnt
day_index = day_name.index(a)
cnt = 0

diff_na = diff % 7
diff //= 7


if diff_na >= day_index:
    cnt += 1
cnt += diff

print(cnt)



