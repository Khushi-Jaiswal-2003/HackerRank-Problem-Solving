a = int(input("Enter range"))
b = []
for i in range(a):
    x = input().split()
    b.append(x)
print(b)
r = 0
for i in range(len(b)):
    r+=int(b[i][i])
print(r)
s = 0
s1=1
for i in range(len(b)):
    w = len(b[i])-s1
    s1+=1


    s+=int(b[i][w])

print(s)
q = r-s
if q<0:
    print(-q)
else:
    print(q)