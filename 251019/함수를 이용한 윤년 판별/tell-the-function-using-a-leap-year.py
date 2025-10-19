y = int(input())

# Please write your code here.

def is_yun(y):
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        return False
    else:
        return True

if is_yun(y):
    print('true')
else:
    print('false')