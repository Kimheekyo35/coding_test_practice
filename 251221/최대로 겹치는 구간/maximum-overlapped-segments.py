offset = 100
max_r = 200

n = int(input())

segments = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
list_a = [0] * (max_r + 1)

for x1, x2 in segments:
    x1, x2 = x1+offset, x2+offset

    for i in range(x1,x2):
        list_a[i] += 1

max_num = max(list_a)
print(max_num)


