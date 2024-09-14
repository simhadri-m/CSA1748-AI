from heapq import heappush, heappop
import itertools

# Define the goal state for the 8-puzzle
GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Define the possible moves (up, down, left, right)
MOVES = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def manhattan_distance(state):
    """Calculate the Manhattan distance heuristic for the given state."""
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                goal_r, goal_c = divmod(value - 1, 3)
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def get_neighbors(state):
    """Generate all possible neighbor states from the current state."""
    r, c = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    neighbors = []
    for move, (dr, dc) in MOVES.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [list(row) for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append((new_state, move))
    return neighbors

def a_star_search(start):
    """Perform A* search algorithm to solve the 8-puzzle problem."""
    open_set = []
    heappush(open_set, (0, start, []))
    closed_set = set()
    
    while open_set:
        cost, state, path = heappop(open_set)
        
        if state == GOAL_STATE:
            return path
        
        closed_set.add(tuple(itertools.chain(*state)))
        
        for neighbor, move in get_neighbors(state):
            neighbor_tuple = tuple(itertools.chain(*neighbor))
            if neighbor_tuple in closed_set:
                continue
            
            new_cost = len(path) + 1 + manhattan_distance(neighbor)
            heappush(open_set, (new_cost, neighbor, path + [move]))
    
    return None

def print_state(state):
    """Print the puzzle state in a readable format."""
    for row in state:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

def main():
    start_state = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
    
    print("Initial state:")
    print_state(start_state)
    
    solution = a_star_search(start_state)
    
    if solution:
        print("Solution path:")
        print(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
