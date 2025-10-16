num_list = list(map(int,input().split()))

ascii_list = [chr(number) for number in num_list if 33<=number<=126]

print(*ascii_list)