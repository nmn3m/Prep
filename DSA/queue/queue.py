## Covered method
### is_empyty, enqueue, dequeue, size, peek

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0 
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue size:", queue.size())  # Output: Queue size: 3
    print("Front element (peek):", queue.peek())  # Output: Front element (peek): 10

    # Dequeue elements
    print("Dequeued:", queue.dequeue())  # Output: Dequeued: 10
    print("Dequeued:", queue.dequeue())  # Output: Dequeued: 20

    print("Queue size after dequeues:", queue.size())  # Output: Queue size after dequeues: 1
    print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False

    # Dequeue the last element
    print("Dequeued:", queue.dequeue())  # Output: Dequeued: 30
    print("Is queue empty now?", queue.is_empty())  # Output: Is queue empty now? True