import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost estimate to the goal
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def astar_search(start, goal, grid):
    # Initialize start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)

    # Open and closed sets
    open_list = []
    closed_list = set()

    # Add the start node to the open list
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Check if we reached the goal
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children (neighbors)
        neighbors = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # 4-directional movement
            # Uncomment for 8-directional movement
            # (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        for move in neighbors:
            neighbor_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if not (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0])):
                continue  # Skip out-of-bounds

            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue  # Skip walls

            neighbor_node = Node(neighbor_pos, current_node)
            if neighbor_pos in closed_list:
                continue  # Skip already evaluated nodes

            # Calculate costs
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = abs(neighbor_pos[0] - goal_node.position[0]) + abs(neighbor_pos[1] - goal_node.position[1])
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Check if node is already in open list with a lower f value
            if any(neighbor_pos == node.position and neighbor_node.f >= node.f for node in open_list):
                continue

            # Add the node to the open list
            heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)
    path = astar_search(start, goal, grid)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
