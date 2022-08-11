from typing import Any
from collections import deque

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        stack = [self._root]
        visited = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            for child in node.outbound[::-1]:
                if child not in visited:
                    stack.append(child)
        return visited

    def bfs(self) -> list[Node]:
        queue = deque()
        visited = []
        queue.appendleft(self._root)
        visited.append(self._root)
        while queue:
            node = queue.pop()
            for child in node.outbound:
                if child not in visited:
                    queue.appendleft(child)
                    visited.append(child)
        return visited
