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


def f_iter():
    with open("day_3.in") as f:
        for l in f:
            yield l


inp = list(f_iter())


def count(inp, pos):
    zeros = 0
    ones = 0
    for l in inp:
        if l[pos] == "0":
            zeros += 1
        else:
            ones += 1
    return zeros, ones


def ogr_filter(zeros, ones, d):
    if zeros > ones:
        return d == "0"
    else:
        return d == "1"
    # elif zeros == ones:
    #     return d == '1'


def csr_filter(zeros, ones, d):
    if zeros > ones:
        return d == "1"
    # elif zeros < ones:
    else:
        return d == "0"
    # elif zeros == ones:
    #     return d == '0'


def cut(inp, pos, keep_filter):
    print(pos)
    print(inp)
    if len(inp) < 2:
        return inp

    zeros, ones = count(inp, pos)
    print(zeros, ones)
    keep = [l for l in inp if keep_filter(zeros, ones, l[pos])]
    return cut(keep, pos + 1, keep_filter)


[ogr] = cut(inp, 0, ogr_filter)
[csr] = cut(inp, 0, csr_filter)
ogr = int(ogr, base=2)
csr = int(csr, base=2)

print(csr * ogr)
