# a = [1, 2, 3, 4, 5]
# b = sum(a)
# print(b)
# print(b - max(a))
# print(b - min(a))
data = list(map(int,input().split()))
print(data)
r=[]

for i in range(len(data)):
    el = 0
    for j in range(i+1,len(data)):
        el+=data[j]
    for k in range(i-1,-1,-1):
        el+=data[k]
    r.append(el)
    print(r)
r.sort()
print(r[0],r[-1])
a = list(map(int, input().split()))
c = []
for i in range(len(a)):
    b = 0
    for j in range(i+1,len(a)):
        b+=a[j]
    for k in range(i-1, -1, -1):
        b+=a[k]
    c.append(b)
    print(c)
c.sort()
print(c)
print(c[0], c[-1])