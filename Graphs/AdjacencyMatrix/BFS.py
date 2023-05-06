class BFS:
    def bfs(self, root, grid, target):
        queue = [root, "#"]
        visited = set()
        visited.add(root)
        count = 1
        while len(queue) > 0:

            node = queue.pop(0)
            if node == target:
                return count

            if node == "#":
                count += 1
                if len(queue) != 0:
                    queue.append("#")
                continue

            neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            for neighbor in neighbors:
                nRow = node[0] + neighbor[0]
                nCol = node[1] + neighbor[1]

                if (not self.outOfBounds(nRow, nCol, grid)) and ((nRow, nCol) not in visited) and (
                        grid[nRow][nCol] == 0):
                    visited.add((nRow, nCol))
                    queue.append((nRow, nCol))

        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1
        return self.bfs((0, 0), grid, (len(grid) - 1, len(grid) - 1))

    def outOfBounds(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return True
        return False

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = [root, "#"]
        visited = set([root])
        result = []
        currentLevel = []
        while len(queue) > 0:
            node = queue.pop(0)

            if node == "#":
                result.append(currentLevel)
                if len(queue) != 0:
                    currentLevel = []
                    queue.append("#")

                continue

            currentLevel.append(node.val)

            neighbors = node.children

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return result