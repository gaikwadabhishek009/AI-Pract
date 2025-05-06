import heapq

def calculate_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if col < len(state) and state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

def a_star_n_queens(n):
    # Priority queue with elements: (f(n), state)
    open_list = []
    heapq.heappush(open_list, (0, []))  # (cost, state)

    while open_list:
        _, state = heapq.heappop(open_list)

        if len(state) == n:
            return state  # Solution found

        col = len(state)  # Next column to place a queen
        for row in range(n):
            new_state = state + [row]
            h = calculate_conflicts(new_state)
            g = len(new_state)
            f = g + h
            heapq.heappush(open_list, (f, new_state))

# Solve for 8-queens
solution = a_star_n_queens(8)
print_board(solution)
