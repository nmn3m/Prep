## Mehtod covered
### push, pop, peek, is_empty, size 

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    # Example Usage
    stack = Stack()

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack size:", stack.size())  # Output: Stack size: 3
    print("Top element (peek):", stack.peek())  # Output: Top element (peek): 30

    # Pop elements
    print("Popped:", stack.pop())  # Output: Popped: 30
    print("Popped:", stack.pop())  # Output: Popped: 20

    print("Stack size after pops:", stack.size())  # Output: Stack size after pops: 1
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

    # Pop the last element
    print("Popped:", stack.pop())  # Output: Popped: 10
    print("Is stack empty now?", stack.is_empty())  # Output: Is stack empty now? True
