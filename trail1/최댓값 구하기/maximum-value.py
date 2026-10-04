a, b, c = map(int,input().split())

# if a>=b and a>=c:
#     print(a)

# elif b>=a and b>=c:
#     print(b)

# else:
#     print(c)

# 우선 a=b or a>b
if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
# a<b
else:
    if b<=c:
        print(c)
    else:
        print(b)