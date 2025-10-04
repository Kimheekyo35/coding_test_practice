n = int(input())

string = [input() for _ in range(n)]

total_elem=0
a_cnt=0
for elem in string:
    total_elem += len(elem)
    if elem[0] == 'a' :
        a_cnt += 1

print(total_elem, a_cnt)