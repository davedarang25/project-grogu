# stack.py

class Stack:
    def __init__(self):
        self.history = []

    def push(self, action):
        """Push an action onto the stack."""
        self.history.append(action)

    def pop(self):
        """Pop the most recent action from the stack."""
        if not self.isEmpty():
            return self.history.pop()
        return None

    def peek(self):
        """View the most recent action without removing it."""
        if not self.isEmpty():
            return self.history[-1]
        return None

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.history) == 0
