from collections import deque

# Sample Graph: A connected to B and C, etc.
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Frank'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Frank'],
    'Frank': ['Charlie', 'Eve']
}

def get_k_degrees_bfs(start_node, k):
    visited = {start_node}
    queue = deque([(start_node, 0)])
    results = []

    while queue:
        person, dist = queue.popleft()
        
        if 0 < dist <= k:
            results.append((person, dist))
        
        if dist < k:
            for neighbor in graph.get(person, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
    return results

# Usage
print(get_k_degrees_bfs('Alice', 2)) 