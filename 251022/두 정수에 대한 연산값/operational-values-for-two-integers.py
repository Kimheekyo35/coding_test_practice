a,b = map(int,input().split())

def plus(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    return a,b

x, y = plus(a,b)
print(x,y)