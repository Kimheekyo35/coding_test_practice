M, D = map(int, input().split())

# Please write your code here.

def month_day31(M, D):
    s_n = str(M)
    if s_n == ('1' or '3' or '5' or '7' or '8' or '10' or '11'):
        for i in range(1,32):
            if D == i:
                return True
    elif s_n == '2':
        for i in range(1,29):
            if D == i :
                return True

    elif M >= 13 or D >= 32:
        return False
    
    else:
        for i in range(1,31):
            if D == i:
                return True

    return False

if month_day31(M,D):
    print("Yes")
else:
    print("No")