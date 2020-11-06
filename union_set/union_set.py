class UnionSet:
    def __init__(self, n: int):
        self._father = [i for i in range(n)]

    def find(self, v: int) -> int:
        _v = v
        while self._father[_v] != v:
            _v = self._father[_v]
        while self._father[v] != _v:
            temp = self._father[v]
            self._father[v] = _v
            v = temp
        return _v

    def union(self, a: int, b: int) -> int:
        fat_a = self.find(a)
        fat_b = self.find(b)
        self._father[fat_a] = fat_b
        return fat_b
