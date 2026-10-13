cnt = 0
for _ in range(10):
    num = int(input())
    # if num % 2 != 0:
    #     cnt += 1
    if num%2:
        cnt += 1
    # num == 0 -> False
    # 0이 아니면 다 True
print(cnt)