n = int(input())
a = list(map(int, input().split()))

prev_max_idx=n

#첫 번째 원소가 최대가 되기 전까지 계속 반복함.
# while True면 break가 나올 때까지 무한루프

#계속 반복되는 문제에선 while문 사용.
while True:
    #최대값 후보의 시작은 항상 첫번째 원소
    max_idx=0

    for i in range(1,prev_max_idx):
        if a[i]>a[max_idx]:
            max_idx=i

    print(max_idx+1,end=' ')

    if max_idx==0:
        break

    prev_max_idx=max_idx

            
