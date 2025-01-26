# Obtain an iterator from the string
string = "hello"
string_iterator = iter(string)

# Use the next function to get elements from the iterator
print(next(string_iterator))  # Output: 'h'
print(next(string_iterator))  # Output: 'e'
print(next(string_iterator))  # Output: 'l'
print(next(string_iterator))  # Output: 'l'
print(next(string_iterator))  # Output: 'o'

# If you call next again, it will raise StopIteration
#incorrect next usage on string wthich is iterable not iterator does not have next method defined
print(next(string))
try:
    print(next(string_iterator))
except StopIteration:
    print("End of string reached")