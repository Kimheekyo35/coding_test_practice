m1, d1, m2, d2 = tuple(map(int,input().split()))

monthly_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

day_name = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

m1d1_sumday, m2d2_sumday = 0, 0

for i in range(1,m1):
    m1d1_sumday += monthly_day[i]
m1d1_sumday += d1

for i in range(1,m2):
    m2d2_sumday += monthly_day[i]
m2d2_sumday += d2


diff_under_7 = True

diff_day = m2d2_sumday - m1d1_sumday


while True:
    diff_day %= 7
    if diff_day < 7:
        break

print(day_name[diff_day])



