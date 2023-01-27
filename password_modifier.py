word = input()
password = ''

for character in word:
    if character == 'i':  # Replaces i with the number 1
        password += '1'
    elif character == 'a':  # Replaces a with the @ symbol
        password += '@'
    elif character == 'm':  # Replaces m with a capital M
        password += 'M'
    elif character == 'B':  # Replaces B with the number 8
        password += '8'
    elif character == 's':   # Replaces s with the $ symbol
        password += '$'
    else:
        password += character  # Takes the original password and adds the replacement characters

# Prints out the new password and adds the ! symbol at the end
print(password + '!')
