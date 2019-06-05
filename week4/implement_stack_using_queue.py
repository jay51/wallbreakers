class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        queue = []
        queue.insert(0, x)
        for idx in range(len(self.stack)):
            queue.insert(0, self.stack.pop())
            
        self.stack = queue
        print(self.stack)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #print(self.stack)
        return self.stack.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.stack)
    
