a, b, c = map(int, input().split())

# Please write your code here.
# min 이 60 넘어가면 hours += 1, hours가 24 넘어가면 day += 1



def calculate(a,b,c):
    day = 11
    time = 11
    fix_min = 11
    time_count = 0

    if day > a and time > b and fix_min > c:
        return -1
    
    while True:
        time_count += 1
        fix_min += 1
        
        if day == a and time == b and fix_min == c:
            return time_count
            break
        
        if fix_min == 60:
            time += 1
            fix_min = 0
        
        if time == 24:
            day += 1
            time = 0
print(calculate(a,b,c))