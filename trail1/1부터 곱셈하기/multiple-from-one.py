n = int(input())
prob = 1
for i in range(1,11):
    prob *= i
    if prob >= n:
        print(i)
        break

