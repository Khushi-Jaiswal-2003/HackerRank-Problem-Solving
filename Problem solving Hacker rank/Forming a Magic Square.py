
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# diagonal_1= []
# diagonal_2 = []
# for i in range(len(s)):
#     diagonal_1.append(s[i][i])
#     diagonal_2.append(s[i][len(s)-1-i])
# print(sum(diagonal_1))
# print(diagonal_2)
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
data = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
t =[]
for i in data:
    res =0
    for j, k in zip(i, s):
        # print("J AND K",j, k)
        for x, y in zip(j, k):
            # print(x, y)
            print("Max",max([x, y]))
            print("Min",min([x, y]))
            res += max([x, y])-min([x, y])
            print(res)
    t.append(res)
print(min(t))