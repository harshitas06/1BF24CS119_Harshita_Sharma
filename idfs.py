# IDFS / IDDFS for 8-Puzzle

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)   # 0 represents the blank space

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

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with the tile
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


# Depth Limited Search
def depth_limited_search(state, goal, depth, path, visited):

    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for next_state in get_neighbors(state):

        if next_state not in visited:

            result = depth_limited_search(
                next_state,
                goal,
                depth - 1,
                path + [next_state],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


# Iterative Deepening DFS
def IDFS(start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        visited = set()

        result = depth_limited_search(
            start,
            goal,
            depth,
            [start],
            visited
        )

        if result is not None:
            return result

    return None


# Main program

start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = IDFS(start, goal, 20)


if solution:

    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):

        print("Step", step)
        print_puzzle(state)

else:

    print("No solution found within the given depth.")