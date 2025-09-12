arr=list(map(int,input().split()))

new_arr=[i for i in arr if (i!=-999) and (i!=999)]

print(max(new_arr),min(new_arr))