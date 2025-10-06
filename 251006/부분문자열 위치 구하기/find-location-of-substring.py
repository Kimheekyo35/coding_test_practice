input_str = input()
target_str = input()

cnt = 0
# Please write your code here.
for i in range(len(input_str)-len(target_str)+1):
    if input_str[i:i+len(target_str)] == target_str[:]:
        cnt += 1

if cnt:
    print(cnt)
else:
    print("-1")

