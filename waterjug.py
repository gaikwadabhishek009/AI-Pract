from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))  # Start with both jugs empty
    parent = {}  # To track path

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(f"Jug A: {a}L, Jug B: {b}L")  # Print each state

        if a == target or b == target:
            print("\n✅ Goal Reached!")
            return

        # Possible moves
        next_states = [
            (jug1_capacity, b),         # Fill Jug A
            (a, jug2_capacity),         # Fill Jug B
            (0, b),                     # Empty Jug A
            (a, 0),                     # Empty Jug B
            (min(a + b, jug1_capacity), b - (min(a + b, jug1_capacity) - a)),  # Pour B -> A
            (a - (min(a + b, jug2_capacity) - b), min(a + b, jug2_capacity)),  # Pour A -> B
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

# Run the solver
water_jug_bfs(4, 3, 2)
