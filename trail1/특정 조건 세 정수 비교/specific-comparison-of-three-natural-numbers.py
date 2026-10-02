# abc = list(map(int,input().split()))
# min_num = min(abc)

# if abc[0] == min_num:
#     print(1,end=" ")
# else:
#     print(0, end=" ")

# if abc[0] == abc[1] and abc[1] == abc[2]:
#     print(1)
# else:
#     print(0)

a,b,c = map(int,input().split())

if a<=b and a<=c:
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b and b==c:
    print(1)
else:
    print(0)