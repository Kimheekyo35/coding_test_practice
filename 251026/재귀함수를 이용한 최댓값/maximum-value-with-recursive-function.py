n = int(input())
arr = list(map(int, input().split()))

max_value = 0

def find_max(arr_list,n):
    
    global max_value

    if max_value < arr_list[n-1]:
        max_value = arr_list[n-1]
        return find_max(arr_list,n-1)
    
    return max_value

print(find_max(arr_list,n'))
