str = input()

# Please write your code here.
list_str = list(str)
sorted_str = sorted(list_str,key= lambda x: x[0])
sorted_str = "".join(sorted_str)

print(sorted_str)