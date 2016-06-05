my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]

counter = 0

for word in my_words:
    if word not in word_list:
        print(word)
        counter += 1

print("Total new words: %d" % counter)
