string = input()
list_str = list(string)
for _ in range(len(string)-1):
    
    pop_idx = int(input())

    
    
    if len(list_str) == 1:
        break
    elif pop_idx >= len(string):
        list_str.pop(-1)
        print(list_str)
    else:
        list_str.pop(pop_idx)
        print(list_str)



