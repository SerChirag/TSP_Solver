import union
import random
max_length = float("inf")

def tsp(data,G):
    
    MSTree = MST(G)
    odd_vertexes = FOV(MSTree)
    MWM(MSTree, G, odd_vertexes)
    etour = FET(MSTree, G)
    current = etour[0]
    path = [current]
    visited = [False] * len(etour)

    length = 0

    for v in etour[1:]:
        if not visited[v]:
            path.append(v)
            visited[v] = True

            length += G[current][v]
            current = v
    return path

def MWM(MST, G, odd_vert):
    random.shuffle(odd_vert)
    global max_length
    while odd_vert:
        v = odd_vert.pop()
        length = max_length
        u = 1
        closest = 0
        for u in odd_vert:
            if v != u and G[v][u] < length:
                length = G[v][u]
                closest = u

        MST.append((v, closest, length))
        odd_vert.remove(closest)

def MST(G):
    tree = []
    subtrees = UnionFind()
    for W, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v, W))
            subtrees.union(u, v)

    return tree

def FET(commonMST, G):
    
    sathi_log = {}
    for edge in commonMST:
        if edge[0] not in sathi_log:
            sathi_log[edge[0]] = []

        if edge[1] not in sathi_log:
            sathi_log[edge[1]] = []

        sathi_log[edge[0]].append(edge[1])
        sathi_log[edge[1]].append(edge[0])

    start_vertex = commonMST[0][0]
    EP = [sathi_log[start_vertex][0]]

    while len(commonMST) > 0:
        for i, v in enumerate(EP):
            if len(sathi_log[v]) > 0:
                break
        while len(sathi_log[v]) > 0:
            w = sathi_log[v][0]
            REM(commonMST, v, w)
            del sathi_log[v][(sathi_log[v].index(w))]
            del sathi_log[w][(sathi_log[w].index(v))]
            i += 1
            EP.insert(i, w)
            v = w
    return EP

def REM(MatchedMST, vertex1, vertex2):

    for i, item in enumerate(MatchedMST):
        if (item[0] == vertex2 and item[1] == vertex1) or (item[0] == vertex1 and item[1] == vertex2):
            del MatchedMST[i]

    return MatchedMST

def FOV(MST):
    temporaryG = {}
    odd_vertexes = []
    for edge in MST:
        if edge[0] not in temporaryG:
            temporaryG[edge[0]] = 0

        if edge[1] not in temporaryG:
            temporaryG[edge[1]] = 0

        temporaryG[edge[0]] += 1
        temporaryG[edge[1]] += 1

    for vertex in temporaryG:
        if temporaryG[vertex] % 2 == 1:
            odd_vertexes.append(vertex)
    return odd_vertexes

