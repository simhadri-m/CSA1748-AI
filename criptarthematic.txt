from itertools import permutations

# Function to check if a solution is valid
def is_valid_solution(solution, word1, word2, result):
    # Map letters to their corresponding digits
    mapping = {letter: digit for letter, digit in zip(solution[0], solution[1])}

    # Convert words to their numerical values based on the mapping
    num1 = int("".join(str(mapping[letter]) for letter in word1))
    num2 = int("".join(str(mapping[letter]) for letter in word2))
    num_result = int("".join(str(mapping[letter]) for letter in result))

    # Check if the sum of num1 and num2 equals num_result
    return num1 + num2 == num_result

# Function to solve the cryptarithmetic problem
def solve_cryptarithmetic(word1, word2, result):
    # Extract unique letters from all words
    letters = set(word1 + word2 + result)

    # Ensure there are not more than 10 unique letters (0-9 digits)
    if len(letters) > 10:
        print("Too many unique letters to solve with digits 0-9.")
        return

    # Try all permutations of the digits for the letters
    for perm in permutations('0123456789', len(letters)):
        if is_valid_solution((letters, perm), word1, word2, result):
            # Map letters to digits
            solution = {letter: digit for letter, digit in zip(letters, perm)}
            print("Solution found!")
            print("Mapping:", solution)
            return solution

    print("No solution found.")
    return None

# Example usage: Solve SEND + MORE = MONEY
word1 = "SEND"
word2 = "MORE"
result = "MONEY"

solve_cryptarithmetic(word1, word2, result)
