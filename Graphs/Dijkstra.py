import heapq
class  Dijkstra :
    def dijkstra(self, graph, source, dist) :
        visited = set()
        minHeap = [(0,source)]
        dist[source] = 0
        count = 0
        ans = 0
        while len(minHeap) > 0 :
            tup = heapq.heappop(minHeap)
            node = tup[1]
            if node in visited :
                continue

            visited.add(node)

            neighbors = graph.get(node,[])

            for neighbor in neighbors :
                weight = neighbor[1]
                if dist[node] + weight <  dist[neighbor[0]] :
                    dist[neighbor[0]] = dist[node] + weight
                    ans = max(ans,dist[node] + weight)

                    heapq.heappush(minHeap,(dist[neighbor[0]],neighbor[0]))

    def networkDelayTime(self, times: List[List[int]], n: int, source: int) -> int:
        if source is None:
            return None

        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = [(time[1], time[2])]
            else:
                graph[time[0]].append((time[1], time[2]))
        distances = [float('inf')] * (n + 1)

        self.dijkstra(graph, source, distances)

        for d in distances[1:]:
            if d == float("inf"):
                return -1
        return max(distances[1:])