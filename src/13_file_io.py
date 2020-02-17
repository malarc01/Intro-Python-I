"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# f = open("foo.txt", 'r').read()

# f.read()

# with open('foo.txt') as f:
#     read_data = f.read()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open("bar.txt", "w+")
f.write("Now the file has content.")
f.close()
f = open("bar.txt", "r")
print('PRINTING:', f.read())
f = open('bar.txt', "a")
f.write(" This is a second line.")
f.write(" This is the last line.")
f.close()
f = open("bar.txt", "r")
print('- PRINT =>', f.read())
