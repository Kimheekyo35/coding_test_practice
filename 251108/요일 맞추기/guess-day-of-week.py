m1, d1, m2, d2 = map(int, input().split())

month_day_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

#총 일
def calculate_day(month,day):
    today_days = 0
    for i in range(1,month):
        today_days += month_day_list[i]
    today_days += day

    return today_days

# if (m1 > m2) or ((m1 == m2) and (d1 > d2)):
diff = calculate_day(m2,d2) - calculate_day(m1,d1)

while True:
    diff %= 7
    if abs(diff) < 7:
        break

print(day_list[diff])
