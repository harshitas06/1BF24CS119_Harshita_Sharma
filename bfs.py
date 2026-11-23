from collections import deque


# Print the puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Generate all possible moves
def get_neighbors(state):

    neighbors = []

    # Find blank space (0)
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    # Up, Down, Left, Right
    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid position
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            # Create a new state
            new_state = list(state)

            # Swap blank with tile
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


# BFS function
def BFS(start, goal):

    # Queue stores (current_state, path)
    queue = deque()

    queue.append((start, [start]))

    # Keep track of visited states
    visited = set()

    visited.add(start)

    while queue:

        # Remove the first element
        state, path = queue.popleft()

        # Check if goal is reached
        if state == goal:
            return path

        # Generate possible next states
        for next_state in get_neighbors(state):

            if next_state not in visited:

                visited.add(next_state)

                queue.append(
                    (next_state, path + [next_state])
                )

    return None


# Starting state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Call BFS
solution = BFS(start, goal)


# Print solution
if solution:

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):

        print("Step", step)
        print_puzzle(state)

else:

    print("No solution found.")