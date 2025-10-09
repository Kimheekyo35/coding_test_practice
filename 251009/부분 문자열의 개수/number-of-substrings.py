input_str = input()
target_str= input()

cnt = 0
for i in range(len(input_str)-1):
    if input_str[i:i+2] == target_str:
        cnt += 1

print(cnt)