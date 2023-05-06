class DFS :
    def dfs(self, root, target, graph, visited):
        if root == target:
            return True

        visited.add(root)
        neighbors = graph[root]

        for neighbor in neighbors:
            if neighbor not in visited:
                if self.dfs(neighbor, target, graph, visited):
                    return True

        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])

        return self.dfs(source, destination, graph, set())