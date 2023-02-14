a = int(input())
b = list(map(int, input().split()))
Min = 0
Max = 0
min_score = b[0]
max_score = b[0]
for i in range(1, len(b)):
    if min_score > b[i]:
        min_score=b[i]
        Min+=1
    elif max_score < b[i]:
        max_score=b[i]
        Max+=1
print(Max, Min)
