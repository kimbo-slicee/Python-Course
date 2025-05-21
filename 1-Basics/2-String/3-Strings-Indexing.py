# Strings Indexing
# ------------------
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# How to access String Elements
# Example
# Get the character at position 1 (remember that the first character has position 0):
string ="hello world !"
print(string[0]) #Index 0 ===> h
print(string[-1]) # negative value start form end !
# Slicing (Accessing Multiple Sequence Items)
# [Start:End] !NOTE: End Not Included
# [Start:End:Steps]
print(string[3:8]) #lo wo
print(string[:10]) # if there is no start it's a start form index 0
print(string[5:]) # if there is no End it's to the end of the string
print(string[:])# full string
#slicing with steps
print(string[::1]) # this will return full string with default step 1
print(string[::2]) # the output is hlowrd! why 🤔 the step 2 men's skip two chars and
print(string[::3])



