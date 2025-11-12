n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
len_commands = len(commands)
n_list = [0]+[0]*n

# commands 각각 튜플
for tup in range(len_commands):
    # (5,5) 일 때 5 탐색
    # for i in range(len(commands[tup])):
    #     n_list[commands[tup][i]] += 1
    start = commands[tup][0]
    end = commands[tup][1]+1

    for i in range(start,end):
        n_list[i] += 1
    # if n_list[commands[tup][0]:commands[tup][1]+1]

print(max(n_list))