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




from collections import deque
#we use sets for faster lookup in the
# 1. The Social Graph
# Keys are people, values are sets of friends
social_network = {
    'Alice': {'Bob', 'Charlie', 'Diana'},
    'Bob': {'Alice', 'Eve', 'Frank'},
    'Charlie': {'Alice', 'Eve'},
    'Diana': {'Alice', 'Frank', 'Grace'},
    'Eve': {'Bob', 'Charlie', 'Heidi'},
    'Frank': {'Bob', 'Diana', 'Heidi'},
    'Grace': {'Diana'},
    'Heidi': {'Eve', 'Frank'}
}

def get_connections_with_ai_ranking(graph, start_person, k_limit):
    if start_person not in graph:
        return "Person not found in network."

    # BFS Setup
    visited = {start_person}
    queue = deque([(start_person, 0)])
    potential_connections = []

    while queue:
        current_person, dist = queue.popleft()

        # If we are within the degree limit (but not the person themselves)
        if 0 < dist <= k_limit:
            # AI HEURISTIC: Calculate mutual friends for ranking
            # intersection find common items between two sets
            start_friends = graph[start_person]
            current_friends = graph[current_person]
            mutual_friends = start_friends.intersection(current_friends)
           
            potential_connections.append({
                'name': current_person,
                'degree': dist,
                'mutual_count': len(mutual_friends),
                'mutual_names': list(mutual_friends)
            })

        # Continue BFS if we haven't reached the k limit
        if dist < k_limit:
            for neighbor in graph.get(current_person, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

    # Sort by: 1. Closest Degree, 2. Highest number of Mutual Friends
    ranked_results = sorted(
        potential_connections,
        key=lambda x: (x['degree'], -x['mutual_count'])
    )
   
    return ranked_results

# --- User Input Section ---
print("--- Social Network Discovery ---")
user_start = input("Enter start person (e.g., Alice): ").strip()
user_k = int(input("Enter max degrees of separation (k): "))

results = get_connections_with_ai_ranking(social_network, user_start, user_k)

# --- Output Section ---
if isinstance(results, str):
    print(results)
else:
    print(f"\nResults for {user_start} (up to {user_k} degrees):")
    print(f"{'Name':<10} | {'Degree':<8} | {'Mutual Friends'}")
    print("-" * 40)
    for person in results:
        mutuals = ", ".join(person['mutual_names']) if person['mutual_names'] else "None"
        print(f"{person['name']:<10} | {person['degree']:<8} | {person['mutual_count']} ({mutuals})")

