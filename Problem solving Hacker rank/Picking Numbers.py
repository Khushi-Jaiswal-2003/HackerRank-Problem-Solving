n = int(input())
a = list(map(int, input().split()))
a1 = list(set(a))
res = []
for i in range(len(a1)):
    x = []
    for j in range(len(a)):
        if a1[i]-a[j]==0:
            x.append(a[j])

        if a1[i]-a[j]==1:
            x.append(a[j])
    res.append(x)
# print(res)

final_res = {}
for i in range(len(res)):
    final_res[len(res[i])]= res[i]
# print(final_res)

print(max(final_res.keys()))

