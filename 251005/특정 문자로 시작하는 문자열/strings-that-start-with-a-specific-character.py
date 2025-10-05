n = int(input())

string_list = [input() for _ in range(n)]

alpha=input()

total = 0
cnt = 0
for string in string_list:
    if string[0] == alpha:
        total += len(string)
        cnt += 1
total /= cnt

print(cnt, f"{total:.2f}")