# here generator object used 
# which returns an object that is both iterator and iterable, 
# so returns self each time iter is called.
def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# Assign two variables to iter(gen)
iterator1 = iter(gen)
iterator2 = iter(gen)

# Check if they point to the same object
print(iterator1 is iterator2)  # Output: True

# Use the first iterator
print(next(iterator1))  # Output: 1
print(next(iterator1))  # Output: 2

# Use the second iterator (same as the first one)
print(next(iterator2))  # Output: 3

##here string is used which is only an iterable,
#  has no next method and iter returns a new iterator object each time not just itself
# Create a string
my_string = "hello"

# Obtain two independent iterators from the string
iterator1 = iter(my_string)
iterator2 = iter(my_string)

# Check if they point to different objects
print(iterator1 is iterator2)  # Output: False

# Use the first iterator
print(next(iterator1))  # Output: 'h'
print(next(iterator1))  # Output: 'e'

# Use the second iterator (independent of the first one)
print(next(iterator2))  # Output: 'h'
print(next(iterator2))  # Output: 'e'