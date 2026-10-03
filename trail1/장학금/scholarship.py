mid, final = map(int,input().split())

if mid>=90 and final>=95:
    print(100000)
elif mid>=90 and final>=90:
    print(50000)
else:
    print(0)