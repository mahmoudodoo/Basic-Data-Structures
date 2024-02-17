
# Example: Using a dictionary for a simple phone book
phone_book = {'Alice': '123-456-7890', 'Bob': '987-654-3210'}
print(f"Alice's phone number: {phone_book['Alice']}")

# Example: Using a queue to manage print tasks
from collections import deque
print_tasks = deque(['document1', 'document2', 'document3'])
print(f"Next print task: {print_tasks.popleft()}")

# Example: Using a stack to reverse a string
def reverse_string(s):
    stack = list(s)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string

print(f"Reversed string: {reverse_string('hello')}")
