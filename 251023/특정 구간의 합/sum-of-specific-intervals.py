n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def cal_q(k):
    a, b = k[0],k[1]
    return a-1,b

def sum_val():
    for q in queries:
        val = 0
        a1, a2 = cal_q(q)
        val = arr[a1:a2]
        print(sum(val))

sum_val()
