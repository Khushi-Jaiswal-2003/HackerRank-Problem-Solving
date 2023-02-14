n = int(input())
shared = 5
cummulative =0
for i in range(1,n+1):
    day = i
    liked_ad = shared // 2
    cummulative+=liked_ad
    # print(day, shared, liked_ad, cummulative)
    shared=liked_ad*3
print(cummulative)