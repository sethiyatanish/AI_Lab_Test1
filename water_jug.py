from collections import deque


def water_jug(capacity_a, capacity_b, target):
    # Check whether the target is possible
    if target < 0 or target > max(capacity_a, capacity_b):
        print("Target cannot be achieved with these jug capacities.")
        return

    # Each state represents (amount of water in jug A, amount in jug B)
    start = (0, 0)

    # Queue stores states and their paths
    queue = deque([(start, [start])])

    # Keep track of visited states
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        # Check whether we have reached the target
        if a == target or b == target:
            print("\nSolution found!")
            print("Total steps:", len(path) - 1)

            for step, state in enumerate(path):
                print(
                    f"Step {step}: Jug A = {state[0]} litres, "
                    f"Jug B = {state[1]} litres"
                )

            return

        # Generate all possible next states

        # 1. Fill Jug A
        next_states = [(capacity_a, b)]

        # 2. Fill Jug B
        next_states.append((a, capacity_b))

        # 3. Empty Jug A
        next_states.append((0, b))

        # 4. Empty Jug B
        next_states.append((a, 0))

        # 5. Pour Jug A into Jug B
        pour = min(a, capacity_b - b)
        next_states.append((a - pour, b + pour))

        # 6. Pour Jug B into Jug A
        pour = min(b, capacity_a - a)
        next_states.append((a + pour, b - pour))

        # Add unvisited states to the queue
        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    print("No solution exists for these capacities and target.")


# Take input from the user
capacity_a = int(input("Enter capacity of Jug A: "))
capacity_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

# Run the program
water_jug(capacity_a, capacity_b, target)
