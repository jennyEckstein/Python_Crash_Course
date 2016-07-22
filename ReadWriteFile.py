import os
# wb is permissions for write and read
test_file = open("test.txt", "wb")
print test_file.mode

print test_file.name

# does not work for some reason
# test_file.write(bytes("Write me to the file\n", "UTF-8"))
# test_file.close()

# read from file
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print text_in_file


# remove the file
# os.remove("test.txt")
