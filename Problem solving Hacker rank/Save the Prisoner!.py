# prisoner = 3
# candies = 7
# chair = 3
# position =[]
# count = 1
# i =1
# while count<=candies:
#     if chair==prisoner+1:
#         # position.append(chair)
#         i=1
#         chair=1
#         position.append(i)
#     else:
#         position.append(chair)
#     count+=1
#     i+=1
#     chair+=1
# print(len(position))
# print(position)
# print(position[-1])

test_cases = int(input())
test_list = []
for i in range(test_cases):
    x = list(map(int, input().split()))
    test_list.append(x)
final_position = []
for i in range(len(test_list)):
    position = []
    prisoner = test_list[i][0]
    candies = test_list[i][1]
    chair = test_list[i][2]
    count = 1
    i=1
    while count<=candies:
        if chair==prisoner+1:
            # position.append(chair)
            i=1
            chair=1
            position.append(i)
        else:
            position.append(chair)
        count+=1
        i+=1
        chair+=1
    final_position.append(position)
# print(final_position)
for i in final_position:
    print(i[-1])