from typing import List, Tuple
from dataclasses import dataclass, field
from queue import PriorityQueue


@dataclass(order=True)
class QueueNode:
    distance: int
    node: int = field(compare=False)

    def __init__(self, node, distance):
        super().__init__()
        self.node = node
        self.distance = distance


def dijstra(adj: List[Tuple[int, int]], v: int):
    n = len(adj)
    dis = [None] * n
    dis[v] = 0

    queue = PriorityQueue()
    queue.put(QueueNode(v, 0))

    inq = [False] * n
    inq[v] = True

    while queue.qsize() != 0:
        node = queue.get()
        v, distance = node.node, node.distance
        inq[v] = False
        for adj_node in adj[v]:
            node_v, node_distance = adj_node
            if dis[node_v] is None or dis[node_v] > distance + node_distance:
                dis[node_v] = distance + node_distance
                if not inq[node_v]:
                    inq[node_v] = True
                    queue.put(QueueNode(node_v, distance + node_distance))
    return dis


dijstra([[(0, 0)]],
        0)
