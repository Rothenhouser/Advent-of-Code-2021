from dataclasses import dataclass


@dataclass
class Pos:
    depth: int
    horiz: int


pos = Pos(0, 0)

cmds = {
    'forward': lambda x, p: Pos(p.depth, p.horiz + x),
    'up': lambda x, p: Pos(p.depth - x, p.horiz),
    'down': lambda x, p: Pos(p.depth + x, p.horiz),
}

with open('day_2.in') as f:
    for l in f:
        cmd, x = l.split(' ')
        x = int(x)
        pos = cmds[cmd](x, pos)


print(pos)
print(pos.horiz * pos.depth)
