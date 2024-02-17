
# Example: Working with Dictionaries
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(f"Original dictionary: {my_dict}")

# Accessing items
print(f"Name: {my_dict['name']}")

# Adding a new key-value pair
my_dict['email'] = 'john@example.com'
print(f"Dictionary after adding email: {my_dict}")

# Example: Using Sets
my_set = {1, 2, 3, 4, 5}
print(f"Original set: {my_set}")

# Adding an item to the set
my_set.add(6)
print(f"Set after adding an element: {my_set}")

# Set operations
another_set = {4, 5, 6, 7, 8}
print(f"Union: {my_set.union(another_set)}")
print(f"Intersection: {my_set.intersection(another_set)}")
