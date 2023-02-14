# queue using queue module

from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of he Queue
print(q.qsize())

#Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Removing elements from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty)

q.put(1)
print("\nEmpty: ",q.empty())
print("Full: ",q.full())

# This would result into Infinite
# Loop as the Queue is Empty,
# print(q.get())
