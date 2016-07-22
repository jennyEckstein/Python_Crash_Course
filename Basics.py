print("Hello World")

# Comment

'''
    Multiline Comment
'''

# Variable declaration
# For stirngs you can use single and double quotes
name = "Jenny"
print(name)

# 5 main types of data in Python
# Numbers
# Strings
# Lists
# Tuples
# Dictionaries

# There are 7 arithmetic functions

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2) # exponent
print("5 // 2 = ", 5//2) # divide and discard remainder

# Order of operations matters
print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)

# Having a quote in String
quote = "\"Always remember you are unique\""
print(quote)

# You can create multiline quotes
# Lines are preserved
multi_line_quote = '''  Line 1
                        Line 2
                        Line 3
'''

add_strings = quote + multi_line_quote
print(add_strings)

# Formatting technique for printing
print("%s %s %s" % ("Line 0", quote, multi_line_quote))

# Stop printing a new line, not working on my
# print("I don't like ", end="")


# Print multiple new lines
print('\n' * 5)