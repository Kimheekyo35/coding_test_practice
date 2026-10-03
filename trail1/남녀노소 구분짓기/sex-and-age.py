# 0 = 남자
# 1 = 여자
# 19 이상 = 성인

gen_num = int(input())
age = int(input())

if gen_num == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")