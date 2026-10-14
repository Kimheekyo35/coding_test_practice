a, b = map(int,input().split())
prob = 1
for i in range(a,b+1):
    prob *= i

print(prob)