queries = int(input())
location=[]
for i in range(queries):
    x = list(map(int, input().split()))
    location.append(x)

count_A=0
count_B=0
win = []
for i in range(len(location)):
    while True:
        if location[i][0]== location[i][2]:
            break

        else:
            if location[i][0] <location[i][2]:
                count_A += 1
                location[i][0] += 1

            else:
                count_A += 1
                location[i][0] -= 1

    while True:
        if location[i][1] == location[i][2]:
            break

        else:
            if location[i][1] < location[i][2]:
                count_B += 1
                location[i][1]+= 1
            else:
                count_B += 1
                location[i][1] -= 1

    print(count_A, count_B)

    if count_A > count_B:
        win.append("Cat B")

    elif count_A < count_B:
        win.append("Cat A")

    elif count_A == count_B:
        win.append("Mouse C")
    count_A=0
    count_B=0

for i in win:
    print(i)
