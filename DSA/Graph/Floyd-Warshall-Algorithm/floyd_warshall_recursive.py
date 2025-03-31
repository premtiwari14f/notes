import sys

def floyd_warshall_recursive(graph, i, j, k):
    if k == -1:
        return graph[i][j]  # Base case: return direct distance

    # Consider the shortest path through vertex k or ignore it
    without_k = floyd_warshall_recursive(graph, i, j, k - 1)
    with_k = (floyd_warshall_recursive(graph, i, k, k - 1) + 
              floyd_warshall_recursive(graph, k, j, k - 1))

    return min(without_k, with_k)

def floyd_warshall(graph):
    n = len(graph)
    dist = [[sys.maxsize] * n for _ in range(n)]

    # Initialize the distance matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Compute shortest paths recursively
    result = [[floyd_warshall_recursive(dist, i, j, n - 1) for j in range(n)] for i in range(n)]
    
    return result

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 3, sys.maxsize, 5],
        [2, 0, sys.maxsize, 4],
        [sys.maxsize, 1, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 2, 0]
    ]

    shortest_paths = floyd_warshall(graph)

    for row in shortest_paths:
        print(row)
