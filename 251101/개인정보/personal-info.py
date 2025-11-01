n = 5

class person:
    def __init__ (self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight
    def __str__ (self):
        return f"{self.name} {self.height} {self.weight}"

info_list = []
for _ in range(n):
    n, h, w = input().split()
    info_list.append(person(n,int(h),float(w)))

# 이름
info_list.sort(lambda x:x.name)
print("name")
for i in info_list: print(i)
print()
# 키
height_list = sorted(info_list,key=lambda x:-(x.height))
print("height")
for h in height_list: print(h)