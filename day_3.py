inp = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

zeros = [0, 0, 0, 0, 0]
ones = [0, 0, 0, 0, 0]


def f_iter():
    with open("day_3.in") as f:
        for l in f:
            yield l


inp = f_iter()
zeros = [0] * 12
ones = [1] * 12

for l in inp:
    for i, bit_str in enumerate(l):
        if bit_str == "0":
            zeros[i] += 1
        elif bit_str == "1":
            ones[i] += 1

gamma = int("".join("0" if z > o else "1" for z, o in zip(zeros, ones)), base=2)
epsilon = int("".join("0" if z < o else "1" for z, o in zip(zeros, ones)), base=2)
print(gamma)
print(gamma * epsilon)
