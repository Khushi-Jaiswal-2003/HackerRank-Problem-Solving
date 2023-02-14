# ranked = [100, 100, 50, 40, 40, 20, 10]
n = int(input())
ranked = list(map(int, input().split()))
b = len(ranked)
# player = [5, 25, 50, 120]
m = int(input())
player= list(map(int, input().split()))
a =0
res = []
for i in range(b):
    if len(player)==a:
        break
    else:
        ranked.append(player[a])
        ranked = list(set(ranked))
        ranked.sort()
        ranked.reverse()
        v = ranked.index(player[a])
        res.append(v+1)
        ranked.remove(player[a])
        a+=1
        # player.remove(player[a])
        # print(ranked)
print(res)




