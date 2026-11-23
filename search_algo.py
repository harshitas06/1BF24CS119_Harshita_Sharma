import heapq

def astar(graph, heuristic, start, goal):

    pq = []
    heapq.heappush(pq, (heuristic[start], start))

    g = {start: 0}
    parent = {start: None}

    while pq:

        f, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g[goal]

        for neighbor, cost in graph[current]:

            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:

                g[neighbor] = new_g
                f = new_g + heuristic[neighbor]

                parent[neighbor] = current

                heapq.heappush(pq, (f, neighbor))

    return None, float('inf')



graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 12)],
    'C': [('B', 1), ('D', 8)],
    'D': [('E', 3)],
    'E': []
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 2,
    'E': 0
}

path, cost = astar(graph, heuristic, 'A', 'E')

print("Shortest Path:", path)
print("Total Cost:", cost)