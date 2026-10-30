
from collections import deque


def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Check the number of people on both sides
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    # Left bank: missionaries must not be outnumbered
    if m_left > 0 and c_left > m_left:
        return False

    # Right bank: missionaries must not be outnumbered
    if m_right > 0 and c_right > m_right:
        return False

    return True


def solve():
    # State: (missionaries_left, cannibals_left, boat_position)
    # boat_position: 0 = left, 1 = right
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = {start}

    # Possible boat passengers: (missionaries, cannibals)
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()
        m_left, c_left, boat = state

        # Goal reached
        if state == goal:
            print("Solution found!")
            print("Total crossings:", len(path) - 1)

            for step, (m, c, b) in enumerate(path):
                side = "Left" if b == 0 else "Right"

                print(
                    f"Step {step}: Left bank: {m} missionaries, "
                    f"{c} cannibals | "
                    f"Right bank: {3-m} missionaries, "
                    f"{3-c} cannibals | Boat: {side}"
                )

            return

        for m, c in moves:
            # Check whether the boat has enough passengers
            if boat == 0:
                # Boat is on the left bank
                new_m = m_left - m
                new_c = c_left - c
                new_boat = 1
            else:
                # Boat is on the right bank
                new_m = m_left + m
                new_c = c_left + c
                new_boat = 0

            new_state = (new_m, new_c, new_boat)

            # Check whether the move is safe and not visited
            if is_valid(new_m, new_c) and new_state not in visited:
                # Passengers must be available on the departure bank
                if boat == 0 and (m > m_left or c > c_left):
                    continue

                if boat == 1:
                    m_right = 3 - m_left
                    c_right = 3 - c_left

                    if m > m_right or c > c_right:
                        continue

                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution found.")


solve()
