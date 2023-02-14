a = 2
b = 1
c = 1
d = 2
e = 0
f = 0
d1 = []
for i in range(1000):
    a+=b
    e+=1
    c+=d
    f+=1
    if a==c and e==f:
       d1.append("Yes")
       break
    else:
        d1.append("No")

print(d1)
if "Yes" in d1:
    print("YES")
else:
    print("NO")

# todo with user input
a = input().split()
e = 0
f = 0
d1 = []
for i in range(10000):
    a[0]= int(a[0])+int(a[1])
    e+=1
    a[2] = int(a[2])+int(a[3])
    f+=1
    if a[0]==a[2] and e==f:
       d1.append("Yes")
       break
    else:
        d1.append("No")

if "Yes" in d1:
    print("YES")
else:
    print("NO")

# todo 2nd method
x1,v1,x2,v2 = map(int,input().split())
jump1 = 0
jump2 = 0
while True:
    x1+=v1
    jump1+=1
    x2+=v2
    jump2+=1
    print(x1,x2)
    if jump1 == jump2 and x1==x2:
        print("Yes")
        break
    if jump1 == jump2 and x1!=x2:
        print("NO")
        break