n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

str.sort()
str_list = []
for text in str:
    if text[0:len(t)] == t:
        str_list.append(text)
print(str_list[k-1])