import random
import math

def calculate_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def random_neighbor(state):
    """Move one queen to a new row in its column."""
    n = len(state)
    new_state = list(state)
    col = random.randint(0, n - 1)
    new_row = random.randint(0, n - 1)
    while new_row == new_state[col]:
        new_row = random.randint(0, n - 1)
    new_state[col] = new_row
    return new_state

def simulated_annealing(n, max_steps=10000):
    temperature = 100.0
    cooling_rate = 0.99
    state = [random.randint(0, n - 1) for _ in range(n)]

    for step in range(max_steps):
        current_conflicts = calculate_conflicts(state)
        if current_conflicts == 0:
            break  # Solution found

        neighbor = random_neighbor(state)
        neighbor_conflicts = calculate_conflicts(neighbor)

        delta = neighbor_conflicts - current_conflicts

        if delta < 0:
            state = neighbor
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                state = neighbor

        temperature *= cooling_rate

    return state

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

# Solve for 8 queens
solution = simulated_annealing(8)
print_board(solution)
