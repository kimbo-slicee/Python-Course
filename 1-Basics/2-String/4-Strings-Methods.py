# String Methods
# --------------
# 1 len (length)
a="I love Pyhon"
print(len(a)) # len return the length of the string and length it's always past index by One
b="    I Love Python  "
print(len(b)) # 19
print(b.strip())  # remove the white spaces form end and start
print(b.rstrip()) # remove white spaces from right
print(b.lstrip()) # remove left spaces
# withe params
c="###Remove#Charchter###"
print(c.strip("#"))
print(c.rstrip("#"))
print(c.lstrip("#"))
# title()
d="i Love 2D Graphics and 3g Technology and python"
print(d.title()) # Make ech string start Character UpperCase even the character after numbers
# capitalize
print(d.capitalize()) # just the first character of all the string
e,f,g="1","11","111"
print(e.zfill(3))
print(f.zfill(3))
print(g.zfill(4))
#upper
h="Hello World!"
print(h.upper()) # HELLO WORLD!
#lower
print(h.lower()) # hello world!


