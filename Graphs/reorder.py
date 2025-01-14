from collections import *
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # we will traverse the graph from 0 and every time we found a child unreachable f
