count_num = input()

list_num = [input() for _ in range(int(count_num))]
sum_num = 0

for i in list_num:
    sum_num += int(i)

print(str(sum_num)[1:] + str(sum_num)[0])