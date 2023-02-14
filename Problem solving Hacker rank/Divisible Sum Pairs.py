x = list(map(int, input().split()))
a = list(map(int, input().split()))
k = x[1]
c = []
for i in range(len(a)):
    b = []
    b.append(a[i])
    for j in range(i+1, len(a)):
        b.append(a[j])
        b = tuple(b)

        c.append(b)
        b = list(b)
        b.remove(b[1])
c = list(c)
d = 0
for i in range(len(c)):
    if sum(c[i])%k ==0:
        d+=1
print(d)


