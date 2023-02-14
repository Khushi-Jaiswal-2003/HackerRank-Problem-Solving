n = int(input())
p = list(map(int, input().split()))
ans = []
for i in range(1, len(p)+1):
    x = i
    a = p.index(i)
    # print(a + 1)
    b = p.index(a+1)
    ans.append(b+1)
for i in ans:
    print(i)
