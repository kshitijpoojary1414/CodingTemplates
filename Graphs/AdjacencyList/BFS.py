class BFS:
    def bfs(self, root, destination, graph):
        visited = {root: 1}
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)

            if node == destination :
                return True

            neighbors = graph.get(node, [])

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited[neighbor] = 1
                    queue.append(neighbor)

            visited[root] = 2
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        if source == destination:
            return True

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        print(graph)
        return self.bfs(source, destination, graph)





