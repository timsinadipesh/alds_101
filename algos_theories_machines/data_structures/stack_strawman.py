"""
Strawman implementation of a stack
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0

    
# Test
stack = Stack()

print("Stack is empty:", stack.is_empty())

[stack.push(x) for x in range(10, 40, 10)]

print(stack.peek())

print("Stack is empty:", stack.is_empty())

item = stack.pop()

print(stack.peek())

for _ in range(3):
    try:
        item = stack.pop()
        print("Popped item:", item)
    except IndexError as e:
        print("Error:", e)

print("Stack is empty:", stack.is_empty())