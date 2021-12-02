from dataclasses import dataclass, replace


@dataclass
class Pos:
    depth: int
    horiz: int
    aim: int


pos = Pos(0, 0, 0)

cmds = {
    "forward": lambda x, p: Pos(p.depth + p.aim * x, p.horiz + x, p.aim),
    "up": lambda x, p: replace(p, aim=p.aim - x),
    "down": lambda x, p: replace(p, aim=p.aim + x),
}

with open("day_2.in") as f:
    for l in f:
        cmd, x = l.split(" ")
        x = int(x)
        pos = cmds[cmd](x, pos)


print(pos)
print(pos.horiz * pos.depth)
