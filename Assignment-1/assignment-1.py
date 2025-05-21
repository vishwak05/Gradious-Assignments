# Printing the unique words from a input text file in sorted order

# Opening 'input.txt' in read mode
input_file = open('input.txt', 'r')

# Reading the contents of input file
input_txt = input_file.read()

print('The input text is:')
print(f'"{input_txt}"')

# Spliting the String into words by " " white space
# Creating a set of all splitted words
# Sorting the set by their alphabets
words = sorted(set(input_txt.split(" ")))

# Joining the sorted words into a single String
joined_words = " ".join(words)
print("\nThe unique words from input in a sorted order:")
print(f'"{joined_words}"')

# Closing the input text file
input_file.close()