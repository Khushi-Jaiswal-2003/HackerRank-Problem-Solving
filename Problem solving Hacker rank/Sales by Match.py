n = int(input())
arr = list(map(int, input().split()))
set_arr = set(arr)
pair =0
# print(set_arr)
for i in set_arr:
    count = 0
    for j in arr:
        if i == j:
            count+=1
            if count == 2:
                pair += 1
                count=0
print(pair)

