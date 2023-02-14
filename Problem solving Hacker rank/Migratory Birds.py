# a1 =int(input())
# a = list(map(int, input().split()))
# b = []
# for i in range(len(a)):
#     b.append(0)
# for i in range(len(a)):
#     b[a[i]]+=1
# print(b.index(max(b)))
#
#
# a1 =int(input())
# a = list(map(int, input().split()))
# b = []
# for i in range(len(a)):
#     b.append(0)
# for i in a:
#     b[i]+=1
# print(b.index(max(b)))
a = [[1], [2, 3, 4], [4, 5]]
n = int(input())
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==n:
            c = a.index(a[i])
            print(c)





