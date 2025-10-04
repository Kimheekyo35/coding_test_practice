alpha = str(input())

str_list = ["apple","banana","grape","blueberry","orange"]
cnt = 0
for i in range(5):
    if alpha in str_list[i]:
        if str_list[i].index(alpha):
            cnt += 1 
            print(str_list[i])
    else:
        pass

print(cnt)

