import re

PATTERN = r"mul\(\d+,\d+\)"

def read_file():
    with open("3_input.txt") as f:
        return f.read()

def mul(str):
    str = str[4:-1]
    a, b = map(int, str.split(","))
    return a * b

def part_one(data):
    multiplications = re.findall(PATTERN, data)
    tot = 0
    for m in multiplications:
        tot += mul(m)
    return tot


def find_do_occurrences(data):
    pattern = r"do\(\)"
    matches = re.finditer(pattern, data)
    indices = [match.start() for match in matches]
    return indices

def find_dont_occurrences(data):
    pattern = r"don't\(\)"
    matches = re.finditer(pattern, data)
    indices = [match.start() for match in matches]
    return indices

def part_two(data):
    do_dont_list = ['']*len(data)
    do_occurrences = find_do_occurrences(data)
    dont_occurrences = find_dont_occurrences(data)
    for i in range(len(data)):
        if i in do_occurrences:
            do_dont_list[i] = "do"
        elif i in dont_occurrences:
            do_dont_list[i] = "dont"

    data_list = list(data)
    doing = True
    for i in range(len(data_list)):
        if do_dont_list[i] == "do":
            doing = True
        elif do_dont_list[i] == "dont":
            doing = False
        if not doing:
            data_list[i] = "_"

    data = ''.join(data_list)
    return part_one(data)

if __name__ == "__main__":
    data = read_file()
    # res = part_one(data)
    res = part_two(data)
    print(res)