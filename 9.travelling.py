import itertools

def calculate_total_distance(route, distance_matrix):
    """
    Calculate the total distance of the given route based on the distance matrix.

    :param route: List of cities representing the route
    :param distance_matrix: 2D list where distance_matrix[i][j] is the distance from city i to city j
    :return: Total distance of the route
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Add distance to return to the starting city
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def tsp_bruteforce(distance_matrix):
    """
    Solve the Traveling Salesman Problem using a brute-force approach.

    :param distance_matrix: 2D list where distance_matrix[i][j] is the distance from city i to city j
    :return: Tuple containing the shortest route and its distance
    """
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_route = None

    for route in itertools.permutations(cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance

# Example usage
if __name__ == "__main__":
    # Example distance matrix where distance_matrix[i][j] represents the distance from city i to city j
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, distance = tsp_bruteforce(distance_matrix)
    print("Shortest route:", route)
    print("Total distance:", distance)
