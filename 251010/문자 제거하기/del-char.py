string = input()
# for문 돌 때마다 갱신되므로 for문 밖에다가 정의해야됨
list_str = list(string)
for _ in range(len(string)-1):
    pop_idx = int(input())

#     if pop_idx >= len(string):
#         string = string[:-1]

#     elif len(string) == 1:
#         break
#     else:
#         string = string[:pop_idx] + string[pop_idx+1:]

#     print(string)
    if len(list_str) == 1:
        break
    elif pop_idx >= len(list_str):
        list_str.pop(-1)
        
    else:
        list_str.pop(pop_idx)
    
    arr = "".join(list_str)
    print(arr)




