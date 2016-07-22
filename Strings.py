
long_string = "I'll catch you if you fall - The Floor"
print long_string

# print first 4 characters
print long_string[0:4]
# print 5 last characters
print long_string[-5:]
# print all but 5 last characters
print long_string[:-5]
# cancatenate string with substring
print long_string[:4] + " be there"

# for some reason formatting does not work
# print ("%c is my %s letter and my number %d number is %.5f",
# 'X' 'favorite',  1, .14)
print '\n' * 5

# capitalize
lowercase_string = 'welcome'
print lowercase_string.capitalize()

# returns 33 for char number
# case sensetive, if not found returns -1
print long_string.find('Floor')

numbers = '123'
letters = 'abc'
# check if all letters
print letters.isalpha()
print numbers.isalpha()

# checks if string is numbers
print letters.isalnum() # Hmm? why true, its letters
print numbers.isalnum()

# replace words varianle not updated
print long_string.replace('Floor', 'Ground')
long_string.replace('Floor', 'Ground')
print long_string

extra_white_space = 'hello      '
print extra_white_space.strip()
print 'again'

# put string in a list
quote_list = long_string.split(" ")
print quote_list