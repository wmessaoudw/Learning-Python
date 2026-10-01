def dfs_recursive(graph: dict, start: str, visited: set = None) -> set:
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")  # Action on visit

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


