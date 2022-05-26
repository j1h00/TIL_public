class Queue:
    def __init__(self, items = []):
        self.queue = items
        self.front = -1
        self.rear = -1

    def push(self, item):
        self.queue.append(item)
        self.rear += 1
    
    def pop(self):
        if self.is_empty():
            return "This queue is empty"
        self.front += 1
        return self.queue.pop(self.front)

    def is_empty(self):
        return self.front == self.rear

Q = Queue()
print(Q.queue)
Q.push(1)
print(Q.queue)