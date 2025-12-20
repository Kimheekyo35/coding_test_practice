a, b, c = tuple(map(int,input().split()))

start = 11 + 11*60 + 60*24*10
end = 24*60*(a-1) + b*60 + c

if start<=end:
    print(end-start)
else:
    print(-1)