b = int(input())
a = input().split()

for i in range(len(a)):
    a[i]=int(a[i])
b = len(a)
c = 0
d = 0
e = 0
for i in range(b):
    if a[i]<0:
        c+=1
    elif a[i]>0:
        d+=1
    elif a[i]==0:
        e+=1
c1 =c/b
d1 = d/b
e1 = e/b
print("%.6f" %d1)
print("%.6f" %c1)
print("%.6f" %e1)