from __future__ import annotations
from typing import Tuple


class MinNode:

    def __init__(self, data: Tuple[int, int], next: MinNode = None):
        self.data = data
        self.next = next


class MinStack:
    
    def __init__(self):
        self.head: MinNode = None
        

    def push(self, val: int) -> None:
        if self.head and val > self.head.data[0]:
            min = self.head.data[0]
        else:
            min = val
        tmp = MinNode((min, val), self.head)
        self.head = tmp
        
        

    def pop(self) -> None:
        val = self.head.data[1]
        self.head = self.head.next
        return val
        

    def top(self) -> int:
        return self.head.data[1]
        

    def getMin(self) -> int:
        return self.head.data[0]
   



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(9)
print(obj.top())
print(obj.getMin())
obj.pop()