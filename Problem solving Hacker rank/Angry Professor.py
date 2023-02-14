no_testcases = int(input())
test_case = []
threshold = []
for i in range(no_testcases):
    k = list(map(int, input().split()))
    threshold.append(k)
    n = list(map(int, input().split()))

    test_case.append(n)
# print(test_case)
# print(threshold)
ans = []
for i in range(len(test_case)):
    student = 0
    for j in range(len(test_case[i])):
        if test_case[i][j]<=0:
            student+=1

    print(student, threshold[i][1])
    if student<threshold[i][1]:
        ans.append("YES")

    else:
        ans.append("NO")

for i in ans:
    print(i)




