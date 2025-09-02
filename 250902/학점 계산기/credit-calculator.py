n=int(input())

list_score=list(map(float,input().split()))


sum_score=0
avg_score=0
for score in list_score:
    sum_score+=score
    
avg_score=(sum_score)/len(list_score)
print(f"{avg_score:.1f}")
if avg_score>=4.0:
    print("Perfect")
elif 4.0>avg_score>=3.0:
    print("Good")
else:
    print("Poor")