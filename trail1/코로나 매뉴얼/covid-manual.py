# 증상 ㅇ, 체온 >= 37 -> A
# 증상 x, 체온 >= 37 -> B
# 증상 o, 체온 < 37 -> C
# 증상 x, 체온 < 37 -> D

a_sym, a_tem = input().split()
b_sym, b_tem = input().split()
c_sym, c_tem = input().split()

a_tem, b_tem, c_tem = int(a_tem), int(b_tem),int(c_tem)

if a_sym == "Y" and a_tem >= 37:
    if (b_sym == "Y" and b_tem >= 37) or (c_sym == "Y" and c_tem >= 37):
        print("E")
    else:
        print("N")
else:
    if (b_sym == "Y" and b_tem >= 37) and (c_sym == "Y" and c_tem >= 37):
        print("E")
    else:
        print("N")