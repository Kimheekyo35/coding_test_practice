text = input()
pattern = input()

# Please write your code here.

def start_index():
    len_txt = len(text)
    len_pat = len(pattern)

    for i in range(len_txt-len_pat+1):
        if pattern in text[i:i+len_pat]:
            return i
    return -1

print(start_index())
        