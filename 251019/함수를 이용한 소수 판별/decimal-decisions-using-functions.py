a, b = map(int, input().split())

# Please write your code here.

# 소수 판별 함수
def prime(n):
    # 소수인지 아닌지 알아야 하는 수 - i
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return prime

# 소수 개수 카운트 하기
def count_prime(a,b):
    print_result = 0
    for i in range(a,b+1):
        result = prime(i)
        if result:
            print_result += i
    return print_result


print(count_prime(a,b))


