
def read_file():
    left = []
    right = []
    with open("1_input.txt") as f:
        for line in f:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
    return left, right

def part_one(left, right):
    left.sort()
    right.sort()

    s = 0
    for l, r in zip(left, right):
        s += abs(l-r)

    return s


def part_two(left, right):
    left.sort()
    right.sort()

    s = 0
    for l in left:
        c = 0
        for r in right:
            if r == l:
                c += 1
        s += l*c

    return s


if __name__ == "__main__":
    left, right = read_file()
    # res=part_one(left, right)
    res=part_two(left, right)
    print(res)