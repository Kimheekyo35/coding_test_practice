# a, b, c, d = map(int, input().split())

# # Please write your code here.

# print(((60*c)+d)-((60*a)+b))

a,b,c,d = map(int,input().split())

hours, mins = a,b
elapsed_time = 0

while True:
    if hours== c and mins == d:
        break
    
    elapsed_time += 1
    mins += 1
    
    if mins == 60:
        hours += 1
        mins = 0
    
print(elapsed_time)