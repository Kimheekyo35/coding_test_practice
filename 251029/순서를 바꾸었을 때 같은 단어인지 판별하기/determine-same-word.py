word1 = input()
word2 = input()

# Please write your code here.

# sorted_word1 = sorted(word1,key=lambda x: x[0])
# sorted_word2 = sorted(word2,key = lambda x:x[0])

# if sorted_word1 == sorted_word2:
#     print("Yes")
# else:
#     print("No")

word1_sorted=list(sorted(word1))
if list(sorted(word1)) == list(sorted(word2)):
    print("Yes")
else:
    print("No")