input_str = input()
target_str = input()

idx = 0
# Please write your code here.
for i in range(len(input_str)-len(target_str)+1):
    if input_str[i:i+len(target_str)] == target_str :
        idx = input_str.index(target_str[0])


if idx >= 0:
    print(idx)
else:
    print("-1")
