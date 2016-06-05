from matplotlib import pyplot
import string

data = open("mystery.txt", "r").read()

# Create a dictionary with an entry for each letter in the
# alphabet. The keys are letters and the values will be the counts of
# the number of times a letter has been seen. For now, initialize all
# the counts to 0.
letter_counts = {}
for char in string.ascii_lowercase:
    letter_counts[char] = 0

# Go through each character in `data`, skipping characters that aren't
# letters. For every letter, increment the count stored in
# `letter_counts` for that letter.
for char in data:
    char = char.lower()
    if char in string.ascii_lowercase:
        letter_counts[char] += 1

# Create a bar chart for the letter frequencies.

# dictionaries don't guarantee an order, so get the items out of the
# dictionary and sort them alphabetically for plotting.
frequencies = letter_counts.items()
labels = []
counts = []
for letter, count in sorted(frequencies):
    labels.append(letter)
    counts.append(count)

# `xlocations` is a list of numbers from 0 to the number of
# frequencies we are plotting, in this case 26.
xlocations = range(len(frequencies))
# `width` is the width of a bar in the bar chart.
width = 0.5
# Calculate where along the x-axis the ticks for each bar should
# go. We want ticks to be in the center of bars.
pyplot.xticks([elt + width/2 for elt in xlocations], labels)
# Draw the bars. `counts` is a list of the heights (frequencies) for
# each bar (letter).
pyplot.bar(xlocations, counts, width=width)

pyplot.xlabel("Letter")
pyplot.ylabel("Frequency")
pyplot.title("Letter frequencies in the US Constitution")

pyplot.show()
