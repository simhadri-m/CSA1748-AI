# Define the map coloring problem using a backtracking approach

class CSP:
    def __init__(self, variables, domains, neighbors):
        """
        variables: list of regions (nodes) to color
        domains: dictionary of {region: [allowed colors]}
        neighbors: dictionary of {region: [neighboring regions]}
        """
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.assignments = {}

    def is_consistent(self, var, value):
        """Check if assigning 'value' to 'var' is consistent with the constraints."""
        for neighbor in self.neighbors[var]:
            if neighbor in self.assignments and self.assignments[neighbor] == value:
                return False  # Neighbor already has the same color
        return True

    def backtrack(self):
        """Backtracking search to find a solution."""
        if len(self.assignments) == len(self.variables):
            return self.assignments  # Solution found
        
        unassigned_vars = [v for v in self.variables if v not in self.assignments]
        var = unassigned_vars[0]  # Select the first unassigned variable
        
        for value in self.domains[var]:
            if self.is_consistent(var, value):
                # Assign the value and move to the next variable
                self.assignments[var] = value
                result = self.backtrack()
                if result:  # If a solution is found
                    return result
                # Otherwise, backtrack (remove the assignment)
                del self.assignments[var]
        
        return None  # No solution found

# Define the regions (states or countries) and their neighbors
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania has no neighbors
}

# Define the available colors
colors = ['Red', 'Green', 'Blue']

# Create the domain for each region
domains = {region: colors for region in regions}

# Initialize the CSP with variables, domains, and neighbors
csp = CSP(variables=regions, domains=domains, neighbors=neighbors)

# Run the CSP backtracking search
solution = csp.backtrack()

# Output the solution
if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
