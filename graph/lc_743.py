from typing import List, Tuple
from dataclasses import dataclass, field
from queue import PriorityQueue


# 利用dataclass装饰器来自动生成可比较的class
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

    while queue.qsize() != 0:
        node = queue.get()
        v, distance = node.node, node.distance
        # 利用多次入queue策略,当当前node比目前最优更差的时候,可以确定
        # 一定有更好的在node中被更新过了,故舍弃
        if distance > dis[v]:
            continue
        # 一开始忘记了这里，后面也没有重复进queue的操作，导致WA
        # distance = dis[v]

        for adj_node in adj[v]:
            node_v, node_distance = adj_node
            if dis[node_v] is None or dis[node_v] > distance + node_distance:
                dis[node_v] = distance + node_distance
                # 重复进queue，更合理的方式是自己实现queue，记录节点对应的queue_index，进行node的上浮
                queue.put(QueueNode(node_v, distance + node_distance))
    return dis


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # bug:这里adj里面的所有list都会是一个instance
        adj = [[] for i in range(N)]
        for u, v, w in times:
            u -= 1
            v -= 1
            adj[u].append((v, w))

        dis = dijstra(adj, K-1)
        ans = 0
        for v in dis:
            if v is None:
                return -1
            ans = max(ans, v)
        return ans


# times = [[4, 2, 76], [1, 3, 79], [3, 1, 81], [4, 3, 30], [2, 1, 47], [1, 5, 61], [1, 4, 99], [3, 4, 68], [3, 5, 46], [
#     4, 1, 6], [5, 4, 7], [5, 3, 44], [4, 5, 19], [2, 3, 13], [3, 2, 18], [1, 2, 0], [5, 1, 25], [2, 5, 58], [2, 4, 77], [5, 2, 74]]
# N = 5
# K = 3

# print(Solution().networkDelayTime(times, N, K)
#       )
