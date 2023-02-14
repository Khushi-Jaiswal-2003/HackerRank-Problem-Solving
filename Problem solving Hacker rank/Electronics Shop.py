b = 5
keyboards =[4]
drives = [5]
combination=[]
for i in keyboards:
    for j in drives:
        if i+j<=b:
            combination.append(i+j)
if len(combination)==0:
    print("-1")
else:
    print(max(combination))
