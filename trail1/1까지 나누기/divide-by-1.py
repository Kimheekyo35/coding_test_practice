n = int(input())
answer = n
for i in range(1,n+1):
    answer //= i
    if answer <= 1:
        break

print(i)