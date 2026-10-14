a, b = map(int,input().split())

# print(a**b)

prob = 1
for _ in range(b):
    prob *= a

print(prob)