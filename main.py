# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Elements can be of different data types

'''
Creating a Tuple
'''

# Empty tuple
tuple = ()
# tuple can hold heterogeneous (different) data types
tuple = ("cat", [4, 3, 2], (1, 2, 3))
# Plain comma-separated values are tuples by default
tuple = 1234, 4321, 'hello!'
# single tuple
tuple = 'hello',    # <== note trailing comma
# single tuple parenthesis
# it becomes just a string object without the trailing comma
tuple = ('hello',) #<== note trailing comma
# looks like tuple, but not a tuple
tuple = ('hello') # => <class 'str'>

'''
Access Tuple Elements
'''

# Accessing tuple elements by indexing
tuple = (1234, 4321, 'hello!')
# access with index
tuple[0] # output => 1234
tuple[2] # output => 'hello!'

'''
Negative Indexing
'''

# Access with negative indexing
tuple = (1234, 4321, 'hello!')
tuple[-1] # output => 'hello'
tuple[-3] # output => 1234

'''
Slicing Tuples in Python
'''

fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')


# beginning to end
fruits[:] # output => ('orange', 'apple', 'pear', 'grapes', 'banana')
# index 2 to 5th item
fruits[2:5] # output => ('pear', 'grapes', 'banana')
# remove last 2 items
fruits[:-2] # output => ('orange', 'apple', 'pear')
# return first 2 items
fruits[:2] # output => ('orange', 'apple')
# index 2 to the end
fruits[2:] # output => ('pear', 'grapes', 'banana')
# every nth item
fruits[::2] # output => ('orange', 'pear', 'banana')
# reverse list
fruits[::-1] # output => ('banana', 'grapes', 'pear', 'apple', 'orange')

'''
Changing a Tuple
'''

fruits = ('orange', [1,2,3])
# Attempt to change the immutable type
fruits[0] = 'pear' # output => TypeError: 'tuple' object does not support item assignment
# Change mutable list type
fruits[1][0] = 5
print(fruits) # output => ('orange', [5, 2, 3])

'''
Deleting a Tuple
'''

fruits = ('orange', [1,2,3])
# can't delete items
del fruits[0] # output => TypeError: 'tuple' object doesn't support item deletion
# Can delete the entire tuple
# deletes successfully
del fruits
print(fruits)

'''
Tuple Methods
'''

# only has 2 in-built methods
print(dir(tuple))

fruits = ('orange', 'banana', 'orange')
fruits.count('orange')
fruits.index('banana')