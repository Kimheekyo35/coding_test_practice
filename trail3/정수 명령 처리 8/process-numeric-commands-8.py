N = int(input())
command = []
A = []
revers_A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])

    if line[0] =="push_front":
        revers_A = list(reversed(A))
        revers_A.append(int(line[1]))
        A = list(reversed(revers_A))
    elif line[0] == "push_back":
        A.append(int(line[1]))
    elif line[0] == "pop_front":
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
