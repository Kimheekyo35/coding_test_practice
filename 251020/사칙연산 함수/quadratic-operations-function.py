a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def result_aoc(a,o,c):
    result = 0
    if o == "*":
        result = a*c
    elif o == "/" :
        result = a // c
    elif o == "+" :
        result = a + c
    elif o == "-" :
        result = a - c
    else:
        result = False
    return result

if type(result_aoc(a,o,c)) == int:
    print(f"{a} {o} {c} = {result_aoc(a,o,c)}")
else:
    print(result_aoc(a,o,c))