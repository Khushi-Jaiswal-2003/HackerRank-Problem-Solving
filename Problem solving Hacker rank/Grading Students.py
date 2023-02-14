b = int(input())
a = []
for i in range(b):
    x = int(input())
    a.append(x)

b = a.copy()
for i in range(len(a)):
    if a[i]%5!=0:
        while True:
            if a[i]%5!=0:
                a[i]+=1

            else:
                break

for i in range(len(a)):
    if a[i]-b[i]<3 and b[i]>37:
        print(a[i])
    elif a[i]-b[i]>=3 and b[i]>37:
        print(b[i])
    else:
        print(b[i])
#
# # todo 2nd method
#
# d=int(input())
# marks = []
# grade = []
#
# for i in range(d):
#     n=int(input())
#     marks.append(n)
#
#
# for j in range(len(marks)):
#     e = marks[j]
#     while True:
#
#         if e%5!=0:
#             e+=1
#
#         if e%5 == 0:
#             grade.append(e)
#
#             break
# result = []
# L = len(marks)
# for i in range(L):
#     for j in range(i,i+1):
#         if marks[i]>37:
#             c = grade[i] - marks[j]
#             if c < 3:
#                 result.append(grade[i])
#             elif c >= 3:
#                 result.append(marks[j])
#         else:
#             result.append(marks[i])
# for j in result:
#     print(j)
#
