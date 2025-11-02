n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

class sort_seq:
    def __init__ (self,sort,index):
        self.sort ,self.index = sort, index
    def __str__ (self):
        return f"{self.sort} {self.index}"

sorted_sequence = sorted(sequence)

index_list = []
for i,num in enumerate(sorted_sequence):
    index_list.append(sort_seq(num,i+1))

test = []
for s in sequence:
    for i in index_list:
        if s == i.sort and i.index not in test:
            test.append(i.index)
            break

print(*test)
            