from collections import deque

def bfs(graph, start_node):
    """
    Perform Breadth-First Search (BFS) on a graph starting from start_node.

    :param graph: A dictionary where keys are node names and values are lists of adjacent nodes
    :param start_node: The node from which BFS starts
    :return: A list of nodes in the order they were visited
    """
    visited = set()         # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS
    result = []             # List to store the order of visited nodes

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)   # Mark node as visited
            result.append(node) # Add node to result

            # Enqueue all unvisited adjacent nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    print("BFS traversal order:", bfs(graph, start_node))
