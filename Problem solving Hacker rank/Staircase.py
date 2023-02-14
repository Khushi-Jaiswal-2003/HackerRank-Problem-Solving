a = int(input("Enter a range: "))
for i in range(0, a):
    for j in range(1, a-i):
        print(" ", end="")
    for k in range(0, i+1):
        print("#", end ="")
    print()