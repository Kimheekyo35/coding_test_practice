a, b, c = map(int, input().split())

# Please write your code here.
# min 이 60 넘어가면 hours += 1, hours가 24 넘어가면 day += 1
day = 11
time = 11
fix_min = 11

def calculate_day(a,b,c):
    return ((a)*24*60+(60*b)+c)
# def calculate(a,b,c):
#     time_count = 0

#     while True:
#         if day == a and time == b and fix_min == c:
#             return time_count
#             break
#         time_count += 1
#         fix_min += 1
#         if fix_min == 60:
#             time += 1
#             fix_min = 0
        
#         if time == 24:
#             day += 1
#             time = 0
# print(calculate(a,b,c))
if calculate_day(a,b,c) >= calculate_day(11,11,11):
    print(calculate_day(a,b,c)-calculate_day(11,11,11))
else:
    print(-1)