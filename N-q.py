import random

def calculate_conflicts(state):
    """Count pairs of queens attacking each other."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_best_neighbor(state):
    """Find the best next state with fewer conflicts."""
    n = len(state)
    best_state = list(state)
    min_conflicts = calculate_conflicts(state)

    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row != original_row:
                neighbor = list(state)
                neighbor[col] = row
                conflicts = calculate_conflicts(neighbor)
                if conflicts < min_conflicts:
                    min_conflicts = conflicts
                    best_state = neighbor
    return best_state, min_conflicts

def print_board(state):
    """Prints the chessboard with queens."""
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

def hill_climbing(n):
    state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = calculate_conflicts(state)

    while True:
        next_state, next_conflicts = get_best_neighbor(state)
        if next_conflicts >= current_conflicts:
            break
        state = next_state
        current_conflicts = next_conflicts

    return state

# Solve for 8-Queens and print board
solution = hill_climbing(3)
print_board(solution)
