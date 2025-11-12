n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_elem = segments[0][1]
min_elem = segments[0][0]
for i in range(1,len(segments)):
    if segments[i][1] > max_elem:
        max_elem = segments[i][1]
    if min_elem > segments[i][0]:
        min_elem = segments[i][0]

blocks = [0 for _ in range(min_elem,max_elem+1)]

for start,end in segments:
    for i in range(start,end):
        blocks[i] += 1

print(max(blocks))