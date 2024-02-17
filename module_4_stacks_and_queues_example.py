
# Example: Using a list as a stack
stack = []
stack.append('A')  # Push A
stack.append('B')  # Push B
print("Stack:", stack)
print("Popped item:", stack.pop())  # Pop B
print("Stack after pop:", stack)

# Example: Using deque as a queue
from collections import deque
queue = deque(['A', 'B', 'C'])
queue.append('D')  # Enqueue D
print("Queue:", list(queue))
print("Dequeued item:", queue.popleft())  # Dequeue A
print("Queue after dequeue:", list(queue))
