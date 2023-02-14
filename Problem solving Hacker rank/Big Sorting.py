# arr = list(map(str, input().split()))
# print(sorted(arr))
# arr.sort(key=int)
# for s in arr:
#     print(s)

# n = int(input().strip())
# unsorted = []
# unsorted_i = 0
# for unsorted_i in range(n):
#     print(unsorted_i)
#     unsorted_t = str(input().strip())
#     unsorted.append(unsorted_t)
# # your code goes here
# uc=[]
# for i in unsorted:
#     uc.append(int(i))
# uc.sort()
# for i in uc:
#     print(i)

# n = int(input().strip())
# list_a = []
# for i in range(n):
#     x = str(input().strip())
#     list_a.append(int(x))
# list_a.sort()
# for i in list_a:
#     print(i)
# print(list_a)

a = ['45563325896630058', '456986996220002558', '5550',
     '4']
for i in sorted(int(s) for s in a):
    print(i)
