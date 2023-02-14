n = 10

a = list(str(n))

print(n)

count = 0

for i in a:

    if int(i)==0:
        continue
    elif 124%int(i)==0:
        count+=1

print(count)