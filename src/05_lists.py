# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print('first ', x)
x.append(4)
print('Answer 1 :', x)

# print('first ', x.append(4))


# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x)
x.extend(y)
print('Answer2:', x)
# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# print(x)
x.pop(4)
# x.remove(10)
print("Answer 3 : ", x)
# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
# print(x)
x.insert(5, 99)
print('Answer 4:', x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i * 1000)
