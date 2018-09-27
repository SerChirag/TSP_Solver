class UnionFind:
    def __init__(self):
        self.weights = {}
        self.father = {}

    def __getitem__(self, object):
        if object not in self.father:
            self.father[object] = object
            self.weights[object] = 1
            return object

        path = [object]
        root = self.father[object]
        while root != path[-1]:
            path.append(root)
            root = self.father[root]

        for ancestor in path:
            self.father[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.father)

    def union(self, *objects):
        roots = [self[x] for x in objects]
        max_heavy = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != max_heavy:
                self.weights[max_heavy] += self.weights[r]
                self.father[r] = max_heavy