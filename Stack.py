# demonstrate stack implementation
# using collections.deque

from collections import deque

stack = deque()

# append() function to push
# element in the stack

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

# pop() function to pop
# element from stack in
# LIFO order

print("\nElement popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\n stack after elements are popped:")
print(stack)

# uncommeting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
