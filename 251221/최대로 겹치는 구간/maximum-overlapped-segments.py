n = int(input())
list_a = [0]*(10000+1)

for _ in range(n):
    x1, x2 = tuple(map(int,input().split()))
    x1 += 100
    x2 += 100
    for i in range(x1,x2):
        list_a[i] += 1

print(max(list_a))


