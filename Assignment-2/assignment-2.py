# Counting the number of alphabets and words in sentence

# Reading the input sentence
input_txt = input("Enter the sentence here: ")

# Spliting sentence into list of indiviual characters
chars = list(input_txt)
letters, digits = 0,0

# iterating over each characters
for i in chars:
    # Checking if character is a alphabet
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        letters+=1
    # Checking if character is a number
    elif i >= '0' and i <= '9':
        digits+=1

print(f'LETTERS {letters}')
print(f'DIGITS {digits}')