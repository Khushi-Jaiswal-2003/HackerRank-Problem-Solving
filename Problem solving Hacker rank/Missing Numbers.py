arr_n = int(input())
arr= list(map(int, input().split()))

brr_n = int(input())
brr = list(map(int, input().split()))

missing = set()

for i in brr:
    if i in arr:
        arr.remove(i)

    else:
        missing.add(i)

print(sorted(list(missing)))