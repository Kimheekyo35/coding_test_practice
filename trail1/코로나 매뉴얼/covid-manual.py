# 증상 ㅇ, 체온 >= 37 -> A
# 증상 x, 체온 >= 37 -> B
# 증상 o, 체온 < 37 -> C
# 증상 x, 체온 < 37 -> D

a_sym, a_tem = input().split()
b_sym, b_tem = input().split()
c_sym, c_tem = input().split()

sym_list = []

a_tem, b_tem, c_tem = int(a_tem), int(b_tem),int(c_tem)

if a_sym =="Y":
    if a_tem >= 37:
        sym_list.append("A")
    else:
        sym_list.append("C")
else:
    if a_tem >= 37:
        sym_list.append("B")
    else:
        sym_list.append("D")

if b_sym == "Y":
    if b_tem >= 37:
        sym_list.append("A")
    else:
        sym_list.append("C")
else:
    if b_tem >=37:
        sym_list.append("B")
    else:
        sym_list.append("D")

if c_sym == "Y":
    if c_tem >= 37:
        sym_list.append("A")
    else:
        sym_list.append("C")
else:
    if c_tem >= 37:
        sym_list.append("B")
    else:
        sym_list.append("D")

# print(sym_list)

if sym_list.count("A") >= 2:
    print("E")
else:
    print("N")     