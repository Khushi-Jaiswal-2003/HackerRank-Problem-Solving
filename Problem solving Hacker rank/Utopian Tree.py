n = int(input())
x = []
for i in range(n):
    a = int(input())
    x.append(a)
# print(x)
res = []
for i in range(len(x)):
    a = 1
    for j in range(1,x[i]+1):
        if j%2==0:
            a+=1

            # print(j,a)
        else:
            a+=a
            # res.append(a)
            # print(j,a)
    res.append(a)
# print(res)
for i in res:
    print(i)