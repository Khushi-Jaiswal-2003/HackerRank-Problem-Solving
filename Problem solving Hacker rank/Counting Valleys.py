string = "DDUUUDD"
count =0
valley=0
for i in string:
    if i=="U":
        count+=1
        # print(count)
        if count==0:
            valley+=1

    elif i=="D":
        count-=1
        # print(count)
print(valley)
