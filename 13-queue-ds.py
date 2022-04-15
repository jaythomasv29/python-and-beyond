# Queues - Data Structures

# First In First Out
restaurant_waitlist = [1,2,3,4]
print(restaurant_waitlist.pop(0))

# a dq object from Collections Module

from collections import deque
 
queue = deque([])
queue.append(1)
print(queue)
queue.popleft()
print(queue)

if not queue:
    print('queue is empty')

# items = [1,2,3,4]
# items.extend([1,2,3,4])
# print(items)