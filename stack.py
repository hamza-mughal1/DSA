from collections import deque
	

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if self.container:
            return True
        return False

    def size(self):
        return len(self.container)