n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
new_list=[]
max_val=0
val=nums[0]
for i in range(1,n):
    

    if val>nums[i]:
        max_val=val
    elif val<nums[i]:
        val=nums[i]
    elif val==nums[i]:
        max_val=-1


print(max_val)