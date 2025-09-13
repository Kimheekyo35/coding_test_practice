n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

# 아닐 경우의 조건 잘 보기
max_num=-1

for current_num in nums:
    if max_num<current_num:
        count=0


        # nums안에 개수 카운트
        for elem in nums:
            if elem==current_num:
                count+=1
        
        if count==1:
            max_num=current_num
    
print(max_num)
    

