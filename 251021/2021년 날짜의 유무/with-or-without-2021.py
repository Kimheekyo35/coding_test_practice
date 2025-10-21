M, D = map(int, input().split())

# Please write your code here.
def day(D,max_d):
    if D <= 31:
        for i in range(max_d+1):
            if i == D:
                return True
    return False

def month_check(M,D):
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        max_d = 31
        if day(D,max_d):
            return True
    elif M == 2:
        max_d = 29
        if day(D,max_d):
            return True
    
    elif M == 4 or M == 6 or M == 9 or M == 11:
        max_d = 30
        if day(D,max_d):
            return True
    else:
        return False


    return False

if month_check(M,D):
    print("Yes")
else:
    print("No")
