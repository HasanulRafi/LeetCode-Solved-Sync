class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjacencyList = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a,b = eq
            adjacencyList[a].append([b,values[i]])
            adjacencyList[b].append([a,1/values[i]])

        print(adjacencyList)
        def bfs(src, trg):
            if src not in adjacencyList or trg not in adjacencyList:
                return -1

            q = deque()
            visited = set()
            q.append([src,1])
            visited.add(src)

            while q: 
                n, w = q.popleft()

                if n == trg:
                    return w

                for neighbor, weight in adjacencyList[n]:
                    if neighbor not in visited:
                        q.append([neighbor, w * weight])
                        visited.add(n)

            return -1

        return [bfs(query[0], query[1]) for query in queries]

        