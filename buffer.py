import os
import sys


class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """


    def __init__(self, policy):
        policy = policy.upper()
        if policy not in ['FIFO', 'LIFO']:
            raise ValueError()
        self._policy = policy
        self._itemList = []

    def show_last(self):
        return self._itemList[-1]


    def insert(self, item):
        """Insert a item to the buffer"""
        self._itemList.append(item) 

 
    def extract(self):
        """
        Remove an element from the buffer selecting desired policy
        Usage object.extract(policy)
        """
        if len(self) == 0:
            raise BufferEmpty("Empty")
            
       
        if self._policy == "LIFO":
            return self.extract_lifo()

        if self._policy == "FIFO":
            return self.extract_fifo()

        else:
            raise PolicyError("You must set a policy")


    def extract_lifo(self):
        item = self._itemList.pop()
        return item


    def extract_fifo(self):
        item = self._itemList.pop(0)
        return item


    def buffersize(self):
        return len(self._itemList)


    def __len__(self):
        """
        >>> b = Buffer('FIFO')
        >>> assert len(b) == 0
        """
        return self.buffersize()

class BufferEmpty(Exception):
   """
   Exception when Buffer is empty
   """
   pass

class PolicyError(Exception):
    """
    Exception when Policy is wrong or not defined
    """
    pass

