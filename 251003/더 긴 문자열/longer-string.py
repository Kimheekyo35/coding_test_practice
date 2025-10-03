string1, string2 = map(str, input().split())

if len(string1) > len(string2) :
    print(string1, len(string1))

elif len(string1) < len(string2) :
    print(string2, len(string2))

else:
    print("same")
