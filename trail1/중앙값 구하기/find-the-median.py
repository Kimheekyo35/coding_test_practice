a, b, c = list(map(int,input().split()))

# a > b > c -> b
# c > b > a -> b
# b > a > c -> a
# c > a > b -> a
# a > c > b -> c
# b > c > a -> c

if (a >= c and c >= b) or (b >= c and c >= a):
    print(c)
elif (b >= a and a >= c) or (c>=a and a>=b):
    print(a)
else:
    print(b)

