a,b = map(int,input().split())

first, second = 0,0
if a<b:
    first = 1
else:
    first = 0

if a==b:
    second=1
else:
    second=0

print(first,second)
    