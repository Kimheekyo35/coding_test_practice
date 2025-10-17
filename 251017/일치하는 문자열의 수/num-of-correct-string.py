a,b = tuple(input().split())

a = int(a)

str_list = [input() for _ in range(a)]

count = 0

for s in str_list:
    if s == b:
        count += 1

print(count)