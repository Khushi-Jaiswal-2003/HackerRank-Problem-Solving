# a = [2, 6]
# b = [24, 36]
# c = []
# d =[]
# for i in range(101):
#     c.append(a[0])
#     a[0]+=2
#     d.append(a[1])
#     a[1]+=6
# print(c)
# print(d)
# e = []
# f = []
# for i in range(1,25):
#     if 24%i==0:
#         e.append(i)
#     if 36%i==0:
#         f.append(i)
# print(e)
# print(f)
# c1 = []
# d1 = []
# e1 = []
# f1 = []
# for i in range(len(c)):
#     for j in range(len(d)):
#         if c[i]==d[j]:
#             c1.append(c[i])
# print(c1)
#
# for i in range(len(e)):
#     for j in range(len(f)):
#         if e[i]==f[j]:
#             d1.append(e[i])
# print(d1)
#
# for i in range(len(c1)):
#     for j in range(len(d1)):
#         if c1[i]==d1[j]:
#             e1.append(c1[i])
# print(e1)
# x = 0
# for i in range(len(e1)):
#     x+=1
# print(x)

# a = int(input("Enter no."))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_factor = []
b_factor = []
common_numbers = []
max_len = len(a+b)
