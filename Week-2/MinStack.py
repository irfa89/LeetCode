"""
155. Design a stack that supports push, pop, top, and
retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:
    class MinStack:
        def __init__(self):
            self.items = []  
            self.min = []  

        def push(self, x):
            self.items.append(x)
            if len(self.min) == 0 or x <= self.min[-1]:
                self.min.append(x)

        def pop(self):
            if len(self.items) == 0:
                return None
            else:
                if self.items[-1] == self.min[-1]:   self.min.pop()
                return self.items.pop()

        def top(self):
            if len(self.items) == 0:
                return None  
            else:
                return self.items[-1]

        
        def getMin(self):
            if len(self.min) == 0:
                return None 
            else:
                return self.min[-1]
def main():
    obj = MinStack()
    obj.push(5)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

if __name__ == "__main__":
    main()