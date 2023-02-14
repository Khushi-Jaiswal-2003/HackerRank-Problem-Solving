s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'
x = len(s) / 3
x = int(x)
count = 0
y = "SOS" * x
for i in range(len(s)):
    if (s[i] != y[i]):
        count = count + 1
print(count)


# s=input().strip()
# print(sum(1 for i in range(len(s)) if s[i]!="SOS"[i%3]))