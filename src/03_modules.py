"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)
print(sys.argv[0])
print([os.fsencode(arg) for arg in sys.argv])
print([os.fsencode(arg) for arg in sys.argv])


# Print out the OS platform you're using:
# print(sys.getwindowsversion()[0])
print(sys.platform)
print(sys.version_info)
print(sys.version)
# YOUR CODE HERE


# Print out the version of Python you're using:
# YOUR CODE HERE


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

# Return the effective group id of the current process. This corresponds to the “set id” bit on the file being executed in the current process.
print(os.getegid())


print(os.geteuid())  # Return the current process’s effective user id.


print(os.getgid())  # Return the real group id of the current process.
group = '20'
user = 505
# Return the real group id of the current process.
print(os.getgrouplist('20', 505))

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())


# Print out your machine's login name
print(os.getlogin())

# YOUR CODE HERE
