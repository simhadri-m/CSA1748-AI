from collections import deque

# Define the state of the riverbanks
class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left
        self.missionaries_right = 3 - missionaries_left
        self.cannibals_right = 3 - cannibals_left

    def is_valid(self):
        # Valid state means no side has more cannibals than missionaries
        if self.missionaries_left < 0 or self.missionaries_right < 0 or self.cannibals_left < 0 or self.cannibals_right < 0:
            return False
        if self.missionaries_left > 0 and self.missionaries_left < self.cannibals_left:
            return False
        if self.missionaries_right > 0 and self.missionaries_right < self.cannibals_right:
            return False
        return True

    def is_goal(self):
        # The goal is when all missionaries and cannibals are on the right bank
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, other):
        return (self.missionaries_left == other.missionaries_left and
                self.cannibals_left == other.cannibals_left and
                self.boat_left == other.boat_left)

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_left))

    def __str__(self):
        return f"Left(M:{self.missionaries_left}, C:{self.cannibals_left}), Right(M:{self.missionaries_right}, C:{self.cannibals_right}), Boat Left: {self.boat_left}"

# All possible moves
def get_successors(state):
    successors = []
    moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]  # (missionaries, cannibals)
    
    for m, c in moves:
        if state.boat_left:  # Boat on left bank
            new_state = State(state.missionaries_left - m, state.cannibals_left - c, 0)
        else:  # Boat on right bank
            new_state = State(state.missionaries_left + m, state.cannibals_left + c, 1)
        
        if new_state.is_valid():
            successors.append(new_state)
    
    return successors

# BFS to solve the problem
def solve():
    start_state = State(3, 3, 1)  # 3 missionaries, 3 cannibals on the left, boat on left
    frontier = deque([start_state])
    explored = set()
    parent_map = {start_state: None}

    while frontier:
        current_state = frontier.popleft()

        if current_state.is_goal():
            # Goal reached, reconstruct path
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1]

        explored.add(current_state)

        for successor in get_successors(current_state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)
                parent_map[successor] = current_state

    return None

def main():
    solution = solve()
    
    if solution:
        print("Solution found:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
