from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    """Solve the water jug problem using BFS."""
    # Initial state (0, 0) meaning both jugs are empty
    initial_state = (0, 0)
    
    # Queue for BFS, starting with the initial state
    queue = deque([initial_state])
    
    # Set to track visited states
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state = queue.popleft()
        x, y = current_state
        
        # Check if we've reached the target
        if x == target or y == target:
            return True
        
        # Generate all possible next states
        next_states = [
            (capacity1, y),  # Fill Jug 1
            (x, capacity2),  # Fill Jug 2
            (0, y),          # Empty Jug 1
            (x, 0),          # Empty Jug 2
            (x - min(x, capacity2 - y), y + min(x, capacity2 - y)),  # Pour Jug 1 to Jug 2
            (x + min(y, capacity1 - x), y - min(y, capacity1 - x))   # Pour Jug 2 to Jug 1
        ]
        
        # Process each next state
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    # If the queue is exhausted without finding the target
    return False

def main():
    capacity1 = 4  # Capacity of the first jug
    capacity2 = 3  # Capacity of the second jug
    target = 2     # Target amount of water

    if water_jug_problem(capacity1, capacity2, target):
        print(f"Yes, it is possible to measure exactly {target} liters.")
    else:
        print(f"No, it is not possible to measure exactly {target} liters.")

if __name__ == "__main__":
    main()
