import random

N = 4

# Calculate attacking pairs
def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing():

    # Random initial state
    state = [random.randint(0, N-1) for _ in range(N)]

    while True:

        current_cost = cost(state)

        if current_cost == 0:
            return state

        best_state = state
        best_cost = current_cost

        # Check all neighbouring states
        for col in range(N):
            for row in range(N):

                new_state = state.copy()
                new_state[col] = row

                new_cost = cost(new_state)

                if new_cost < best_cost:
                    best_cost = new_cost
                    best_state = new_state

        # No better neighbour found
        if best_cost == current_cost:
            return state

        state = best_state


solution = hill_climbing()

print("Solution:", solution)
print("Conflicts:", cost(solution))

# Display chessboard
for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()