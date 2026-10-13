n = int(input())

classroom = 0
way = 0
toilet = 0

# n = 11 -> 2,4,6,8,10 / 3,6,9 /
for i in range(1,n+1):
    if i % 12 == 0:
        toilet += 1
        continue
    
    if i % 3 == 0:
        way += 1
        continue
        

    if i % 2 == 0:
        classroom += 1

print(classroom, way, toilet)
    

