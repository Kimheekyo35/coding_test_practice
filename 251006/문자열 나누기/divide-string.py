n = int(input())
num_list = list(map(str,input().split()))

num_str = "".join(num_list)
new = ""

for i in range(len(num_str)):
    new += num_str[i]
    if (i+1)%5 == 0:
        print(new)
        new=""

print(new)
