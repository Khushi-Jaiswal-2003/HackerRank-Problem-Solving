k= list(map(int, input().split()))
a = list(map(int, input().split()))
queries =[]
for i in range(k[2]):
    x=int(input())
    queries.append(x)

for i in range(k[1]):
    t=-1
    s = a.pop(t)
    # print(s)
    a.insert(0,s)
# print(a)
for i in range(len(queries)):
    print(a[queries[i]])