class DFS :
    def dfs(self, i,j,graph, visited):
        if (i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0])) :
            return

        if visited[i][j] != 0 :
            return

        if graph[i][j] == "0" :
            return

        visited[i][j] = 1
        directions = [(0,-1),(-1,0),(1,0),(0,1)]

        for direction in directions :
            nRow = i + direction[0]
            nCol = j + direction[1]
            self.dfs(nRow,nCol,graph,visited)
        visited[i][j] = 2
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        graph = grid
        visited = [[0 for i in range(len(graph[0]))] for j in range(len(graph))]
        count = 0
        for i in range(len(graph)) :
            for j in range(len(graph[0])) :
                if visited[i][j] == 0 and grid[i][j] == "1":
                    self.dfs(i,j,graph,visited)
                    count += 1

        return count