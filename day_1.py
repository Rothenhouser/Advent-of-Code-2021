
increased = 0

with open('day_1.in') as f:
    depths = map(int, f)
    prev_depth = next(depths)
    for depth in depths:
        if depth > prev_depth:
            increased += 1
        prev_depth = depth


print(increased)