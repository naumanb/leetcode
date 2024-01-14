class MinStack(object):


    def __init__(self):
        
        self.stack = [] # stack to store values
        self.minStack = [] # stack to store min values during each push/pop

        #Note: both stacks will be of same size during each push/pop operation

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)  # append to stack
        minVal = min(val,self.minStack[-1] if self.minStack else val) # find new min value (compare old min to new val)
        self.minStack.append(minVal) # append new min value

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()