string = input()
for _ in range(len(string)-1):
    
    pop_idx = int(input())

    if pop_idx >= len(string):
        string = string[:-1]
        print(string)
    elif len(string) == 1:
        break
    else:
        string = string[:pop_idx] + string[pop_idx+1:]
        print(string)
    
    
    # if len(list_str) == 1:
    #     break
    # elif pop_idx >= len(string):
    #     list_str.pop(-1)
    #     print(list_str)
    # else:
    #     list_str.pop(pop_idx)
    #     new_string = "".join
    #     print(list_str)




