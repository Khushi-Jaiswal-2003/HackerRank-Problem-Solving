a =  [7, 10]
b = [4, 12]
c = [2, 3, -4]
d  = [3, -2, -4]
for i in range(len(c)):
    c[i]+=b[0]
print(c)

for i in range(len(d)):
    d[i]+=b[1]
print(d)
e = 0
f = 0
for i in range(len(c)):
    if a[0]<=c[i]<=a[1]:
        e+=1

for i in range(len(d)):
    print(d[i])
    if a[0]<=d[i]<=a[1]:
        f+=1

print(e)
print(f)

# todo with user input
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c1 = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
for i in range(len(c)):
    c[i] += b[0]

for i in range(len(d)):
    d[i] += b[1]

e = 0
f = 0
for i in range(len(c)):
    if a[0] <= c[i] and a[1] >= c[i]:
        e += 1

for i in range(len(d)):
    if a[0] <= d[i] and a[1] >= d[i]:
        f += 1

print(e)
print(f)

