alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
h = list(map(int, input().split()))
# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
# word = "zaba"
word = input()
word_list = list(word)
range_alpha = []
# print(word_list)
dict_alpha = {}
for i in range(len(alphabet)):
    dict_alpha[alphabet[i]]=h[i]
# print(dict_alpha)

for i in range(len(word_list)):
    for j, k in dict_alpha.items():
        if word_list[i]==j:
            range_alpha.append(k)
# print(range_alpha)

max_height = max(range_alpha)
area = max_height*len(word)
print(area)