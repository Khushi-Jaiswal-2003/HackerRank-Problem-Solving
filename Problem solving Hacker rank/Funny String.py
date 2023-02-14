s = input()
s_re = s[::-1]
# print(s, s_re)

list_s = []
list_s_re = []

for i in range(len(s)):
    list_s.append(ord(s[i]))
    list_s_re.append(ord(s_re[i]))

final = []
final_1 = []
for i in range(len(list_s)-1):
    final.append(abs(list_s[i]-list_s[i+1]))
    final_1.append(abs(list_s_re[i]-list_s_re[i+1]))
print(final)
print(final_1)

if final == final_1:
    print('Funny')
else:
    print('Not Funny')
