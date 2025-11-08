m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

month_day_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]
def calculate_day(month,day):
    total_day = 0
    
    for i in range(1,month):
        total_day += month_day_list[i]
    total_day += day

    return total_day

day_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

indx = day_list.index(A)

diff = calculate_day(m2,d2) - calculate_day(m1,d1)
count = 0
while True:
    if diff < indx:
        break
    else:
        diff -= 7
    count += 1
print(count)
