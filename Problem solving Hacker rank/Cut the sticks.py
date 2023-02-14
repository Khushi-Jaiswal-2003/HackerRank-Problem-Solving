stick = [5, 4, 4, 2, 2, 8]
a =0
final_ans = []
while True:
    if a == len(stick):
        break
    else:
        stick.sort()
        for i in stick:
            if i==0:
                pass
            else:
                # print(stick)
                zero_count = stick.count(0)
                final_ans.append(len(stick)-zero_count)
                min_stick = i
                for i in range(len(stick)):
                    if stick[i]==0:
                        pass
                    else:
                        stick[i] -= min_stick
                # print(stick)

        a+=1
print(final_ans)