def tsp_nearest_neighbor(graph, start):
    visited = [False] * len(graph)
    path = [start]
    total_cost = 0
    current = start
    visited[current] = True

    for _ in range(len(graph) - 1):
        nearest = None
        min_distance = float('inf')
        for city in range(len(graph)):
            if not visited[city] and 0 < graph[current][city] < min_distance:
                min_distance = graph[current][city]
                nearest = city
        path.append(nearest)
        visited[nearest] = True
        total_cost += min_distance
        current = nearest

    # Return to starting point
    total_cost += graph[current][start]
    path.append(start)

    print("Path:", path)
    print("Total cost:", total_cost)

# Example graph as a distance matrix
# 4 cities: 0, 1, 2, 3
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp_nearest_neighbor(graph, 0)
