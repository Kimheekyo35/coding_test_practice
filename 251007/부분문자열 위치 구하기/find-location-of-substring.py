input_str = input()
target_str = input()

idx = -1
# Please write your code here.
for i in range(len(input_str)-len(target_str)+1):
    if input_str[i:i+len(target_str)] == target_str :
        idx = i


if idx != -1:
    print(idx)
else:
    print("-1")
