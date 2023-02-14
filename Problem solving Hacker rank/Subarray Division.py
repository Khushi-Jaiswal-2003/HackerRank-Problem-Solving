q = int(input())
a = list(map(int, input().split()))
w = input().split()
d = int(w[0])
m = int(w[1])
a1 = a[:m]
a1=tuple(a1)
a2 = []
a2.append(a1)
b1 = []
c = 0
for i in range(m, len(a)):
    a1 =list(a1)
    a1.remove(a1[0])
    a1.append(a[i])
    a1=tuple(a1)
    a2.append(a1)
for i in range(len(a2)):
    if sum(a2[i])==d:
        b1.append(a2[i])
        c+=1
print(c)



