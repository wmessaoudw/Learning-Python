from collections import deque
queue=deque()
#to add an element after the tail of the queue we use enqueue/append
queue.append(5)
#to remove the element at the head we use dequeue/pop
queue.pop()
# we use peek to access head value
#priority queues
import heapq
heap=list()
#we use this to enqueue elements
heapq.heappush(heap,5)
#peek at the smallest element
smallest=heap[0]
#poping element
heapq.heappop(heap)