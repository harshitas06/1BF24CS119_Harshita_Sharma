import random
import math

N = 4

# Calculate number of attacking pairs
def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def simulated_annealing():

    # Random initial state
    state = [random.randint(0, N-1) for _ in range(N)]

    T = 100
    cooling = 0.95

    while T > 0.1:

        current_cost = cost(state)

        if current_cost == 0:
            return state

        # Generate neighbouring state
        new_state = state.copy()

        col = random.randint(0, N-1)
        new_state[col] = random.randint(0, N-1)

        new_cost = cost(new_state)

        delta = new_cost - current_cost

        if delta < 0:
            state = new_state

        else:
            probability = math.exp(-delta / T)

            if random.random() < probability:
                state = new_state

        T = T * cooling

    return state


solution = simulated_annealing()

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