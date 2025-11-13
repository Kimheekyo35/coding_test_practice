n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max_n = 100
lines = [0]*(max_n+1)

for start,end in segments:
    for i in range(start,end+1):
        lines[i] += 1

print(max(lines))