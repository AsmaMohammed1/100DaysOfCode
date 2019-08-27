# Cont'd Talk about String .
# ex of methods using in string

word = " Good ,Morning "


# 1: strip()
# method removes any whitespace from the beginning or the end.
print(word.strip())


# 2: len()
# method returns the length of a string.
print("Numbers of characters:", len(word))

# 3: lower() , upper()
print("small letters: "+word.lower())
print("upper letters: "+word.upper())

# 4: replace()
# method replaces a string with another string.
print('New word:'+word.replace("Morning", "Evening"))

# 5: split()
# method splits the string into substrings if it finds instances of the separator.
print(word.split(","))
