n = int(input())

# Please write your code here.
# cnt = 0 

# def make_cnt(n):
#     global cnt

#     if n == 1:
#         return cnt
#     if n % 2 == 0:
#         cnt += 1
#         return make_cnt(n//2)
#     else:
#         cnt += 1
#         return make_cnt((n*3)+1)
cnt = 0 
def make_cnt(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 0:
        n //= 2
    else:
        n = (n*3) + 1
    cnt += 1
    return make_cnt(n)
print(make_cnt(n))