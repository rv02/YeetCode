from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        [flights[src].append(dest) for [src, dest] in tickets]
        for key, values in flights.items():
            flights[key] = sorted(values, reverse=True)
        result = self.getBestPath(["JFK"], flights, len(flights) - 1)
        
    def getBestPath(self, stack, flights: dict[str, List], n) -> List[str]:
        src = stack.pop()
        if not flights[src]:
            return None
        elif n == 0:
            return flights[src]
        stack.extend(flights[src])

        
        