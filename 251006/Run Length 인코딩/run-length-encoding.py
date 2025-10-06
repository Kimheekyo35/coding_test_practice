A = input()

# Please write your code here.

encoded = ""
curr_char = A[0]
num_char = 1
for target_char in A[1:]:
    if target_char == curr_char :
        num_char += 1
    else :
        encoded += curr_char
        
        # 숫자를 str형태로 변환시킴
        encoded += str(num_char)
        
        curr_char = target_char
        num_char = 1
    
# 맨 마지막꺼는 if,else에서 처리가 안 되니까 이렇게 뺴주기

encoded += curr_char
encoded += str(num_char)

print(len(encoded))
print(encoded)