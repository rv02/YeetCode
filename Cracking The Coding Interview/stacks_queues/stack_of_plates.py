'''
https://leetcode.com/problems/dinner-plate-stacks/
'''
from typing import List

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks: List[List] = [[]]
        self.capacity = capacity
        self.le = [0]
        self.rne = []
        


    def push(self, val: int) -> None:
        if not self.rne or self.rne[-1] < self.le[-1]:
            self.rne.append(self.le[-1])
        self.stacks[self.le[-1]].append(val)
        if len(self.stacks[self.le[-1]]) == self.capacity:
            left = self.le.pop()
            if not self.le:
                self.le.append(left + 1)
                self.stacks.append([])

    def pop(self) -> int:
        if not self.rne:
            return -1
        if self.rne[-1] < self.le[-1]:
            self.le.append(self.rne[-1])
        elem = self.stacks[self.rne[-1]].pop()
        if not self.stacks[self.rne[-1]]:
            self.rne.pop()
        return elem


        

    def popAtStack(self, index: int) -> int:
        if not self.stacks[index]:
            return -1
        elem = self.stacks[index].pop()
        if self.le[-1] > index:
            self.le.append(index)
        if self.rne[-1] == index and not self.stacks[index]:
            self.rne.pop()
        return elem
        


D = DinnerPlates(2);  # Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);
D.pop();
D.pop();
D.popAtStack(0);
print(D.stacks)