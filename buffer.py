import os
import sys

FIFO = 'FIFO'
LIFO = 'LIFO'

class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """

    def __init__(self, policy):
        policy = policy.upper()
        if policy not in [FIFO, LIFO]:
            raise PolicyError("You need provide a policy. Valid policies are FIFO or LIFO")
        self._policy = policy
        self._itemList = []

    def show_last(self):
        if self._policy == LIFO:
            return self._itemList[0]

        if self._policy == FIFO:
            return self._itemList[-1]


    def insert(self, item):
        """
        Insert a item to the buffer
        >>> b.insert()
        """
        self._itemList.append(item)
        

 
    def extract(self):
        """
        Remove an element from the buffer
        Usage object.extract()
        """
        if len(self) == 0:
            raise BufferEmpty("Empty")
            
       
        if self._policy == LIFO:
            return self.extract_lifo()

        if self._policy == FIFO:
            return self.extract_fifo()


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

