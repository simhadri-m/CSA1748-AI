def is_valid(graph, color, node, c):
    # Check if this color assignment is valid for node
    for i in range(len(graph)):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, node):
    # Base case: If all nodes are assigned a color then return true
    if node == len(graph):
        return True

    # Consider this node and try different colors
    for c in range(1, m + 1):
        # Check if assignment of color c to node is fine
        if is_valid(graph, color, node, c):
            color[node] = c

            # Recur to assign colors to the rest of the nodes
            if graph_coloring_util(graph, m, color, node + 1):
                return True

            # If assigning color c doesn't lead to a solution then remove it
            color[node] = 0

    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)  # Initialize color array with 0
    if graph_coloring_util(graph, m, color, 0):
        print("Solution exists: Following are the assigned colors")
        print(color)
    else:
        print("Solution does not exist")

# Example usage
if __name__ == "__main__":
    # Representing the graph as an adjacency matrix
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    m = 3  # Number of colors
    graph_coloring(graph, m)
