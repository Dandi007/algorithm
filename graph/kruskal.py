from dataclasses import dataclass, field
from typing import List

from union_set import UnionSet


@dataclass(order=True)
class EdgeNode:
    distance: int
    va: int = field(compare=False)
    vb: int = field(compare=False)

    def __init__(self, va, vb, distance):
        super().__init__()
        self.va = va
        self.vb = vb
        self.distance = distance


def kruskal(edges: List[EdgeNode], n: int):
    edges = sorted(edges)
    union_set = UnionSet(n)
    cost = 0
    for edge in edges:
        va, vb, dis = edge.va, edge.vb, edge.distance
        fa = union_set.find(va)
        fb = union_set.find(vb)
        if fa != fb:
            cost += dis
            union_set.union(va, vb)
    return cost
