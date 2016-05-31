import string

sonnets = open("sonnets.txt").readlines()
word_set = set([elt.strip() for elt in open("sowpods.txt")])
sonnet_words = set()

def strip_punctuation(word):
    # Remove surrounding punctuation. If there's an apostrophe in the
    # middle of the word, skip it.
    word.replace("-", " ")
    apostrophe_index = word.find("'")
    if apostrophe_index != -1:
        return None
    return word.strip(string.punctuation)

for line in sonnets:
    # Split apart hyphenated words.
    line_words = line.replace("-", " ").strip().split()

    # It's an empty line or a sonnet number; skip it.
    if len(line_words) <= 1:
        continue

    for word in line_words:
        stripped = strip_punctuation(word)
        if stripped and len(stripped) > 1:
            sonnet_words.add(stripped.upper())

sonnet_words = list(sonnet_words)
sonnet_words.sort()

f = open("sonnet_words.txt", "w")
for word in sonnet_words:
    f.write(word + "\n")
f.close()
