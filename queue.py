# queue.py

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue."""
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def isEmpty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
