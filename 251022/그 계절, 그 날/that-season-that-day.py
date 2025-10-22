Y, M, D = map(int, input().split())

# Please write your code here.

def season(M):
    if M <= 12:
        if M in [3, 4, 5]:
            return 'Spring'
        elif M in [6, 7, 8]:
            return 'Summer'
        elif M in [9, 10, 11]:
            return 'Fall'
        else:
            return 'Winter'

def day(Y):
    # 윤년이면 True
    if (Y % 4 == 0) :
        if (Y % 100 != 0) or ((Y % 100 == 0) and (Y % 400 == 0)):
            return True
    return False

    
def check_day(Y,M,D):
    if M <= 12 and D <= 31:
        if M == 2:
            if day(Y):
                max_day = 29
            else:
                max_day = 28
        elif M in [1,3,5,7,10,12]:
            max_day = 31
        else:
            max_day = 30
        return 1 <= D <= max_day
    else:
        False

if check_day(Y,M,D):
    print(season(M))
else:
    print(-1)
    
