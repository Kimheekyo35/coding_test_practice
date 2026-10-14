count_num = 0
N = int(input())

for i in range(1,N+1):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    count_num += 1

print(count_num)