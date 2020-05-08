in_come = "you have chance to known what of this words is longest"
print(in_come)

list_words = in_come.split()

id_longest_word = 0

for i in range(1,len(list_words)):
    if len(list_words[id_longest_word]) < len(list_words[i]):
        id_longest_word = i

print(list_words[id_longest_word])