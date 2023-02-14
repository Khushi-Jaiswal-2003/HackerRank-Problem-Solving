# a = 20
# b = str(a)[::-1]
# print(b)


a = [20, 23, 6]
count = 0
for i in range(a[0], a[1]+1):
    rev = int(str(i)[::-1])
    cal = i-rev
    if cal<=0:
        cal = -(cal)
        # print(cal)
    else:
        cal = cal

    if cal%a[2]==0:
        count+=1
print(count)





