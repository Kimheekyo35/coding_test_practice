n = int(input())

class person:
    def __init__ (self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight
    def __str__ (self):
        return f"{self.name} {self.height} {self.weight}"

info_list = []
for _ in range(n):
    nm, h, w = tuple(input().split())
    info_list.append(person(nm,int(h),int(w)))

info_list.sort(key = lambda x: (x.height,-x.weight))

for i in info_list: print(i)