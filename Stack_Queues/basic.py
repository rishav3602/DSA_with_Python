## Push Pop peek operartions after implementing a stack.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty. Cannot perform pop operation.")
            return None

    def peek(self):
        if not self.is_empty():
            top_item = self.stack[-1]
            print(f"Top item in the stack: {top_item}")
            return top_item
        else:
            print("Stack is empty. Cannot perform peek operation.")
            return None

    def is_empty(self):
        return len(self.stack) == 0



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
stack.peek()
stack.peek()
# print(stack)


## Enqueue, dequeue and peek operations after implementing a queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the Queue.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued {item} from the Queue.")
            return item
        else:
            print("Queue is empty. Cannot perform dequeue operation.")
            return None

    def peek(self):
        if not self.is_empty():
            top_item = self.queue[0]
            print(f"Front item in the Queue: {top_item}")
            return top_item
        else:
            print("Queue is empty. Cannot perform peek operation.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.peek()
queue.peek()
queue.peek()
queue.peek()
