# s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = set(s)
# s.remove()
# print(s.remove(4))
# s.remove(0)
# print(s)

# n = int(input())
# p = int(input())
# d = []
# for p1 in range(1,n+1):
#     d.append(p1)
#
# l = len(d)
# r = []
#
# ran = []
# for i in range(l+1):
#     if i == 0:
#         ran.append(i)
#     if i%2!=0:
#         ran.append(i)
#
# e = 1
# for j in ran:
#     r.append(d[j:e])
#     e+=2
#
#
# for k in r:
#     if len(k) == 0:
#         r.remove(k)
#
#
# # todo search
# front = 0
# end = 0
# r1 = []
# for i in range(len(r)-1, -1, -1):
#     r1.append(r[i])
#
# for i in r:
#     for j in i:
#         if j==p:
#             c = r.index(i)
#             front+=c
#
# for i in r1:
#     for j in i:
#         if j==p:
#             c = r1.index(i)
#             end+=c
#
# if front<end:
#     print(front)
# elif end<front:
#     print(end)
# else:
#     print(front)

n = int(input())
p = int(input())
r = int(p/2)
r1 = int(n/2) - r
print(min(r, r1))