"""
YOU DO NOT NEED TO EDIT THIS.
This is proof of concept
"""

class Queue:
    """
    Code created by Kurt Zimmer
    """
    
    def __init__(self):
        """
        Initializes the queue with a data structure such as a list
        or an array
        """
        self.lst = []

    def size(self):
        """
        Gets the size of the queue
        """
        return len(self.lst)
    
    def isEmpty(self):
        """
        Checks to see if the queue is empty. 
        Returns: True if empty
                 False otherwise
        """
        return len(self.lst) == 0
    
    def dequeue(self):
        """
        Removes an item from the front of the queue and 
        returns it. 
        This implementation checks to make sure the queue is 
        not empty. 
        """
        if not self.isEmpty():
            return self.lst.pop(0)
        else:
            return None
    
    def enqueue(self, item):
        """
        Adds an item to the back of the queue
        """
        self.lst.append(item)
    
    def __str__(self):
        return str(lst)