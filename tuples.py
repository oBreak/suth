# Tuple basic usage (see: https://www.tutorialspoint.com/python/python_tuples.htm)

# Empty tuples

# tup1 = ()
#
# try:
#     print(tup1[0])
# except IndexError:
#     pass

# Numbers

# tup1 = (2,3)
#
# print(tup1[1])

# List of tuples

webtup1 = ('http://www.google.com', 'Google')
webtup2 = ('http://www.espn.com', 'ESPN')
webtups = [webtup1, webtup2]

print(webtups[1][0])

