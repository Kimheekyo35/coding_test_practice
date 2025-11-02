n = int(input())

class Distance:
    def __init__ (self, x,y,num,dis):
        self.x, self.y, self.num, self.dis = x, y, num, dis
    def __str__ (self):
        return f"{self.num}"

distance_list = []
for i in range(n):
    d_x, d_y = tuple(map(int,input().split()))
    dis = abs(d_x-0) + abs(d_y -0)
    distance_list.append(Distance(d_x,d_y,i+1,dis))

distance_list.sort(key = lambda x: (x.dis,x.num))

for i in distance_list:
    print(i)
    
    