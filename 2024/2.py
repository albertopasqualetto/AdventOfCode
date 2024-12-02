def safety_check(levels):
    safe = True
    if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
        for i in range(1, len(levels)-1):
            if not(1 <= abs(levels[i]-levels[i-1]) <= 3) or not(1 <= abs(levels[i]-levels[i+1]) <= 3):
                safe = False
                break
    else:
        safe = False
    return safe

def part_one():
    with open("2_input.txt") as f:
        count = 0
        for line in f:
            levels = [int(x) for x in line.split()]
            safe = safety_check(levels)
            if safe:
                count += 1
        return count


def part_two():
    with open("2_input.txt") as f:
        count = 0
        for line in f:
            levels = [int(x) for x in line.split()]
            safe = safety_check(levels)
            if not safe:
                for z in range(len(levels)):
                    sublevels = levels[:z] + levels[z+1:]
                    safe = safety_check(sublevels)
                    if safe:
                        break

            if safe:
                count += 1

        return count


if __name__ == "__main__":
    # res=part_one()
    res=part_two()
    print(res)