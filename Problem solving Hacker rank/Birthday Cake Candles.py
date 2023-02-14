a = int(input())
b = list(map(int, input().split()))
c = max(b)
d = 0
for i in range(len(b)):
    if c==b[i]:
        d+=1
print(d)