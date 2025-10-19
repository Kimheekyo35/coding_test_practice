n = int(input())

# Please write your code here.


def print_num(n):
    count = 1
    for _ in range(n):
        for _ in range(n):
            print(count,end =" ")
            count +=1

            if count > 9:
                count = 1
        print()

print_num(n)
