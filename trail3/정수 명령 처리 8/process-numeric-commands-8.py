N = int(input())
command = []
A = []
revers_A = []

# 해당 코드는 알고리즘의 성능 측면엣 비효율적임
# 리스트는 원소들이 메모리사에 연속적으로 저장되는 구조를 가짐. 따라서 pop, append는 O(1)로 처리 가능.

for _ in range(N):
    line = input().split()
    command.append(line[0])

    if line[0] =="push_front":
        # list(reversed(A)) 를 하면 모든 원소를 순회하며 새로운 리스트를 재생성하므로 O(N)만큼이 걸림
        revers_A = list(reversed(A))
        revers_A.append(int(line[1]))
        # 근데 이걸 한번 더 해주므로 또 O(N)만큼이 걸리게 됨.
        A = list(reversed(revers_A))
    elif line[0] == "push_back":
        A.append(int(line[1]))
    elif line[0] == "pop_front":
        # 이거 역시 맨 앞 원소를 꺼내고, 뒤에 것들을 앞으로 당겨야하기때문에 O(N)이 들어감
        print(A.pop(0))
    elif line[0] == "pop_back":
        print(A.pop(-1))
    elif line[0] == "size":
        print(len(A))
    elif line[0] =="empty":
        if len(A)==0:
            print(1)
        else:
            print(0)
    elif line[0] == "front":
        print(A[0])
    else:
        print(A[-1])
