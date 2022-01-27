# https://www.codingninjas.com/codestudio/problems/the-earliest-moment-when-everyone-become-friends_1376604

from operator import itemgetter
from UnionByRank import UnionFind

def minTime(logs, n):
	# Write your code here.
    obj = UnionFind(n)
    logs.sort(key=itemgetter(0))
    for log in logs:
        (time, x, y) = log
        obj.union(x, y)
        if obj.getCount() == 1:
            return time
    return -1


