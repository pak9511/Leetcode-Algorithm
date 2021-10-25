class MinStack:

    def __init__(self):
        self.stack=collections.deque()
        self.min=sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min>val:
            self.min=val
            
    def pop(self) -> None:
        node=self.stack.pop()
        if node==self.min: 
            if len(self.stack)>0:
                self.min=min(self.stack)
            else: self.min=sys.maxsize

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min
