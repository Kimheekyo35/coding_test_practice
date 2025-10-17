a,b = input().split()

count = 0
sum_ab = str(int(a) + int(b))

for i in sum_ab:
    if i == '1':
        count += 1

print(count)