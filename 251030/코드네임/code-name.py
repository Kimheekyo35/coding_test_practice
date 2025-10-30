MAX_N = 5

codenames = []
scores = []
class info():
    def __init__ (self,code_name,score):
        self.code_name = code_name
        self.score = score

for _ in range(MAX_N):
    code_name, score = input().split()
    codenames.append(code_name)
    scores.append(int(score))

min_scores = min(scores)
min_index = scores.index(min_scores)
min_code_name = codenames[min_index]

guard_info = info(min_code_name,min_scores)

print(guard_info.code_name,guard_info.score)
