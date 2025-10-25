n, m = map(int, input().split())
A = list(map(int, input().split()))

def even_idx(m):
    return m // 2

def odd_idx(m):
    return m - 1
    

sum_val = 0
#맨 처음
sum_val += A[m-1]

while m != 1:
    if m % 2 == 0:
        sum_val += A[even_idx(m)-1]
        m = even_idx(m)
    else:
       sum_val += A[odd_idx(m)-1]
       m = odd_idx(m)
    if m == 1:
        break

print(sum_val)