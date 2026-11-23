def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with adjacent tile
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(initial, goal):

    stack = [(initial, [initial])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        # Goal reached
        if state == goal:
            return path

        # Generate next states
        for neighbor in get_neighbors(state):

            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor])
                )

    return None


def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i + 3])

    print()


# Initial puzzle
initial = (
    1, 2, 3,
    4, 5, 6,
    7, 0, 8
)

# Goal puzzle
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# DFS
solution = dfs(initial, goal)


# Print solution
if solution is not None:

    print("DFS Solution")
    print("Number of moves:", len(solution) - 1)
    print()

    for i, state in enumerate(solution):

        print("Step", i)
        print_puzzle(state)

else:

    print("No solution found")