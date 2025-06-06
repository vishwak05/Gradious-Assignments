# Printing the unique words from a input text file in sorted order

# Reading the input text
input_txt = input("Provide the input here: ")

# Spliting the String into words by " " white space
# Creating a set of all splitted words
# Sorting the set by their alphabets
words = sorted(set(input_txt.split(" ")))

# Joining the sorted words into a single String
joined_words = " ".join(words)
print("\nThe unique words from input in a sorted order:")
print(joined_words)