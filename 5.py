from collections import deque

# Define the state of the problem
class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right
        self.boat_right = boat_right

    def is_valid(self):
        if (self.missionaries_left < self.cannibals_left and self.missionaries_left > 0) or (self.missionaries_right < self.cannibals_right and self.missionaries_right > 0):
            return False
        return True

    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, other):
        return (self.missionaries_left == other.missionaries_left and
                self.cannibals_left == other.cannibals_left and
                self.boat_left == other.boat_left and
                self.missionaries_right == other.missionaries_right and
                self.cannibals_right == other.cannibals_right and
                self.boat_right == other.boat_right)

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_left, self.missionaries_right, self.cannibals_right, self.boat_right))

    def __str__(self):
        return (f"Left Bank: M={self.missionaries_left}, C={self.cannibals_left}, Boat={self.boat_left} | "
                f"Right Bank: M={self.missionaries_right}, C={self.cannibals_right}, Boat={self.boat_right}")

def get_neighbors(state):
    neighbors = []
    if state.boat_left:  # Boat is on the left side
        for m, c in [(2, 0), (1, 0), (0, 1), (1, 1), (0, 2)]:
            if 0 <= state.missionaries_left - m <= 3 and 0 <= state.cannibals_left - c <= 3:
                new_state = State(
                    state.missionaries_left - m, 
                    state.cannibals_left - c, 
                    0,
                    state.missionaries_right + m,
                    state.cannibals_right + c,
                    1
                )
                if new_state.is_valid():
                    neighbors.append(new_state)
    else:  # Boat is on the right side
        for m, c in [(2, 0), (1, 0), (0, 1), (1, 1), (0, 2)]:
            if 0 <= state.missionaries_right - m <= 3 and 0 <= state.cannibals_right - c <= 3:
                new_state = State(
                    state.missionaries_left + m, 
                    state.cannibals_left + c, 
                    1,
                    state.missionaries_right - m,
                    state.cannibals_right - c,
                    0
                )
                if new_state.is_valid():
                    neighbors.append(new_state)
    return neighbors

def solve():
    start_state = State(3, 3, 1, 0, 0, 0)
    goal_state = State(0, 0, 0, 3, 3, 1)
    
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state.is_goal():
            return path + [current_state]
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    
    return None

def main():
    solution = solve()
    
    if solution:
        print("Solution found:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()











