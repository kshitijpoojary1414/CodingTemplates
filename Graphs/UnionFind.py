class UnionFind:
    def __init__(self, size):
        self.root = []
        self.rank = []
        self.size = size
        for i in range(size):
            self.root.append(i)
            self.rank.append(1)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.size -= 1
        else:
            return False
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count(self):
        return self.size

