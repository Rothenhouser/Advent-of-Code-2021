import collections

increased = 0

with open("day_1.in") as f:
    # double-ended queues can be very efficient for moving windows
    # because of fast append/pop
    depths_in_window = collections.deque()
    depths = map(int, f)
    depths_in_window.append(next(depths))
    depths_in_window.append(next(depths))

    prev_avg_depth = 0
    print(depths_in_window)
    for depth in depths:
        depths_in_window.append(depth)
        avg_depth = sum(depths_in_window) / 3
        if avg_depth > prev_avg_depth:
            increased += 1
        prev_avg_depth = avg_depth
        print(depths_in_window)
        depths_in_window.popleft()

print(increased - 1)  # start is edge case
