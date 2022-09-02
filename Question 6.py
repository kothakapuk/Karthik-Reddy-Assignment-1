# Given the String "I am a teacher and I love to inspire and teach people"


str1 = "I am a teacher and I love to inspire and teach people"   # Loaded given string into str1

str1split = str1.split()                                         # Splitting the given string using split() function
print(str1split)                                                 # Printing the string after splitting
result = set(str1split)                                          # Converting the list into set to remove duplicates
print(result)                                                    # Printing the set with unique words
print(" The number of umique words in the given string is " + str(len(result)))  # Printing the number of unique words

