str1, q_num = input().split()
q_num = int(q_num)


for _ in range(q_num):
    num,q1,q2 = input().split()
    num = int(num)
    if num == 1:
        q1 = int(q1)
        q2 = int(q2)
        a = str1[q1-1]
        b = str1[q2-1]


        for i in range(len(str1)):
            if i == q1-1:
                str1 = str1[:i] + b + str1[i+1:]
            elif i == q2-1:
                str1 = str1[:i] + a + str1[i+1:]

        print(str1)

    elif num == 2:
        for i in range(len(str1)):
            if str1[i] == q1:
                str1 = str1[:i] + q2 + str1[i+1:]
        print(str1)
