n = 5
satisfy = True
for i in range(5):
    num = int(input())
    if num%3:
        satisfy = False

if satisfy:
    print(1)
else:
    print(0)
