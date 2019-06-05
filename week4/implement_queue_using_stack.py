class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        stack = []
        stack.append(x)
        for el in range(len(self.queue)):
            stack.append(self.queue[el])
        self.queue = stack
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]
        

    def empty(self) -> bool:
        return not len(self.queue)
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
