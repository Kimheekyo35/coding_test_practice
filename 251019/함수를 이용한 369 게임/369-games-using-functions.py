a, b = map(int, input().split())

# Please write your code here.

def check_369(a,b):
    count = 0
    for i in range(a,b+1):
        i = str(i)
        if '3' in i or '6' in i or '9' in i :
            count += 1
        elif int(i) % 3 == 0:
            count += 1
        else:
            pass
    return count

print(check_369(a,b))