a, b = map(int, input().split())

# Please write your code here.

def cal_ab(x, y):
    if x > y :
        y += 10
        x *= 2
    else:
        x += 10
        y *= 2
    return x, y

a, b = cal_ab(a, b)

print(a,b)
