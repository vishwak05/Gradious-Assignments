# Finding the strength of Password and check if it is acceptable or not

# Function to check the password strength and return strength and acceptable or not
def evaluate_password(password):

    password_strength, password_acceptable = "Weak", True

    # Password is not acceptable if password has incorrect length
    if not 8 <= len(password):
        password_acceptable = False
    
    # Password is not acceptable if password has unacceptable words
    unacceptable_words = ['password', '12345', 'qwerty', 'admin', 'username']
    for word in unacceptable_words:
        if word in password:
            password_acceptable = False

    # Counting number of upper case, lower case, digits, special chars in the password
    upper, lower, digits, special_char = 0, 0, 0, 0

    # Checking indiviual characters in password
    for char in password:
        # Checking if char is alphabet
        if char.isalpha():
            # Checking if char is in upper case
            if char.isupper():
                upper += 1
            # Checking if char is in lower case
            elif char.islower():
                lower += 1
        # Checking if char is a digit
        elif char.isdigit():
            digits += 1
        # If not above conditions are met then it is a speical char
        else:
            special_char += 1

    # Password strength is Strong if all (upper, lower, digit, special) have >= 2 frequency
    if upper >= 2 and lower >= 2 and digits >= 2 and special_char >= 2 and 8 <= len(password):
        password_strength = "Strong"
    
    # Password strength is High if all (upper, lower, digit, special) have >= 1 frequency with anyone of char has >= 2
    elif (upper>=1 and lower>=1 and digits>=1 and special_char>=1 and
          (upper>=2 or lower>=2 or digits>=2 or special_char>=2)) and 8 <= len(password):
        password_strength = "High"
    
    # Password strength is Moderate if all (upper, lower, digit, special) have >= 1 frequency
    elif upper>=1 and lower>=1 and digits>=1 and special_char>=1:
        password_strength = "Moderate"

    # Password Strength is Weak if above conditions are not met
    else:
        password_strength = "Weak"
    
    return password_strength, password_acceptable

# Reading the input Password String
password = input("Enter your password: ")

# Evaluating password strength and acceptable or not
password_strength, password_acceptable = evaluate_password(password)

print(f'Password Strength: {password_strength}')
print(f'Password is Acceptable: {password_acceptable}')