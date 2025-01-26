from collections.abc import Iterable, Iterator
# Define a simple iterable class
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)

# Define an iterator class
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
class NotIterable:
    def __init__(self, data):
        self.data = data

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
# Create an instance of the iterable
my_iterable = MyIterable([1, 2, 3, 4, 5])

# Using the iterable in a for loop
print("Using the iterable in a for loop:")
for item in my_iterable:
    print(item)
# Create an instance of the non-iterable class
not_iterable = NotIterable([1, 2, 3, 4, 5])
# Trying to use the iterator directly in a for loop
print("Trying to use the non-iterable object in a for loop: this is against protocl")
try:
    for item in not_iterable:
        print(item)
except TypeError as e:
    print(f"Error: {e}")