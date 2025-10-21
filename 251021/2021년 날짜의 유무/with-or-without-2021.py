M, D = map(int, input().split())

# Please write your code here.
def day(D,max_d):
    if D <= 31:
        for i in range(max_d+1):
            if i == D:
                return True
    return False

def month_check(M,D):
    if M in [1, 3, 5, 7, 8, 10, 12]:
        max_d = 31

    elif M == 2:
        max_d = 28
    
    elif M in [4,6,9,11]:
        max_d = 30

    else:
        return False

    return 1 <= D <= max_d

if month_check(M,D):
    print("Yes")
else:
    print("No")
