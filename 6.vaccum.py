class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)
        self.cleaned_positions = set()
    
    def move(self, new_position):
        if (0 <= new_position[0] < len(self.grid) and 
            0 <= new_position[1] < len(self.grid[0])):
            self.position = new_position
        else:
            print("Move out of bounds!")
    
    def clean(self):
        x, y = self.position
        if self.grid[x][y] == 1:  # If the current position is dirty
            self.grid[x][y] = 0  # Clean the position
            self.cleaned_positions.add(self.position)
    
    def get_dirty_positions(self):
        dirty_positions = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    dirty_positions.append((i, j))
        return dirty_positions
    
    def find_closest_dirty(self):
        dirty_positions = self.get_dirty_positions()
        if not dirty_positions:
            return None
        closest_dirty = min(dirty_positions, key=lambda pos: abs(pos[0] - self.position[0]) + abs(pos[1] - self.position[1]))
        return closest_dirty
    
    def clean_all(self):
        while self.get_dirty_positions():
            closest_dirty = self.find_closest_dirty()
            if closest_dirty:
                self.move(closest_dirty)
                self.clean()
            else:
                break

    def display_grid(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print()

# Example usage
if __name__ == "__main__":
    # Initialize a 5x5 grid with some dirty positions (represented by 1s)
    grid = [
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]

    vacuum = VacuumCleaner(grid)

    print("Initial Grid:")
    vacuum.display_grid()
    
    vacuum.clean_all()
    
    print("Grid after cleaning:")
    vacuum.display_grid()
    
    print("Positions cleaned:", vacuum.cleaned_positions)
