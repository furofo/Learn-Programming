class MyCombinedIteratorIterable:
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

# Create an instance of the iterable
my_iterable = MyCombinedIteratorIterable([1, 2, 3, 4, 5])

# Obtain two independent iterators from the iterable
iterator1 = iter(my_iterable)
iterator2 = iter(my_iterable)

# Use the next function to get elements from the first iterator
print(next(iterator1))  # Output: 1
print(next(iterator1))  # Output: 2
print(next(iterator1))  # Output: 3
print(next(iterator1))  # Output: 4
print(next(iterator1))  # Output: 5
# Use the next function to get elements from the second iterator
print(next(iterator2))  # Output: 1

# If you call next again, it will raise StopIteration
try:
    print(next(iterator1))
except StopIteration:
    print("End of iterator1 reached")

try:
    print(next(iterator2))
except StopIteration:
    print("End of iterator2 reached")