for i in range(10):
    string = input()
    if string.isalpha() and string != "END":
        print(string[::-1])
    else:
        break