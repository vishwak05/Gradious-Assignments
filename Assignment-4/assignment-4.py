# Printing the words in sorted order of their frequency

# Reading the input sentence
input_txt = input("Provide the sentence here:")

# Splitting the sentence into words
words = input_txt.split(" ")

# Creating a dictionary to count the frequencies of words
words_freq = {}

# Counting the frequency of words
for word in words:
    words_freq[word] = words_freq.get(word, 0) + 1

# Sorting and printing the words in order
for key, value in sorted(words_freq.items()):
    print(f'{key}:{value}')