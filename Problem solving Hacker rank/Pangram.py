s = input()
s = s.split()
s = ''.join(s)
list_a = []
for i in range(len(s)):
    list_a.append(s[i].lower())
# print(len(set(list_a)))
if len(set(list_a)) >= 26:
    print('pangram')
else:
    print('not pangram')

