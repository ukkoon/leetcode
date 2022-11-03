class MinStack:    
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()
        
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)
        
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())