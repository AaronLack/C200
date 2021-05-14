"""
YOU DO NOT NEED TO EDIT THIS.
This is proof of concept
"""

class Stack:

    def __init__(self):
        """
        Initializes the stack as a data structure such as a list or 
        an array
        """
        self.s = []
    

    def pop(self):
        """
        Removes the first item from the stack.
        Implemented so that there is not an error is the start
        is empty
        """
        if self.isEmpty():
            return None
        else:
            return self.s.pop()
    

    def push(self, item):
        """
        Pushes an item on to a stack
        """
        self.s.append(item)
    

    def isEmpty(self):
        """
        Returns True is stack is empty, False otherwise
        """
        return self.s == []
    
    def peek(self):
        """
        Shows what the first item on the stack is. Will keep the stack
        the same, since you just want to see what the value is.
        Returns the item on the top of te stack
        """
        item = self.pop()
        self.push(item)
        return item
    
    def __str__(self):
        return str(self.s)
