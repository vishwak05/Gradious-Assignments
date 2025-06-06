# Printing the number of upper case and lower case letters in sentence

# Reading the input sentence
input_txt = input("Provide the sentence here:")

# Converting the sentence into indiviual characters
chars = list(input_txt)
upper, lower = 0, 0

# Iterating over the indiviual characters
for i in chars:
    # Checking if character is Upper case
    if i >= 'A' and i <= 'Z':
        upper += 1
    elif i >= 'a' and i <= 'z':
        lower += 1

print(f'UPPER {upper}')
print(f'LOWER {lower}')