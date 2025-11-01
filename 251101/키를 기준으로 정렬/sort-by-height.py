n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class human_info:
    def __init__ (self, p_name, p_height, p_weight):
        self.p_name ,self.p_height, self.p_weight = p_name, p_height, p_weight

    def __str__ (self):
        return f"{self.p_name} {self.p_height} {self.p_weight}"

info_list = []

for i in range(n):
    p_info = human_info(name[i],height[i],weight[i])
    info_list.append(p_info)

info_list.sort(key= lambda p_info:p_info.p_height)

for i in info_list:
    print(i)