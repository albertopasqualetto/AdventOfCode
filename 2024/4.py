from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)

def read_file():
    matrix = []
    with open("4_input.txt") as f:
        for line in f:
            row = [char for char in line.strip()]
            matrix.append(row)
    return matrix

def is_xmas(matrix, i, j, dir):
    LENGTH = 4
    for l in range(LENGTH):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return False

        match l:
            case 0:
                if matrix[i][j] != 'X':
                    return False
            case 1:
                if matrix[i][j] != 'M':
                    return False
            case 2:
                if matrix[i][j] != 'A':
                    return False
            case 3:
                if matrix[i][j] != 'S':
                    return False
        i += dir.value[0]
        j += dir.value[1]
    return True

def part_one(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for dir in Direction:
                if is_xmas(matrix, i, j, dir):
                    count += 1
    return count


def is_x_mas(matrix, i, j):
    if i < 1 or i >= len(matrix) - 1 or j < 1 or j >= len(matrix[0]) - 1:
        return False

    if matrix[i][j] == 'A':
        conditions = [
            (matrix[i + Direction.UP_LEFT.value[0]][j + Direction.UP_LEFT.value[1]] == 'M' and
                matrix[i + Direction.DOWN_RIGHT.value[0]][j + Direction.DOWN_RIGHT.value[1]] == 'S'),
            (matrix[i + Direction.UP_RIGHT.value[0]][j + Direction.UP_RIGHT.value[1]] == 'M' and
                matrix[i + Direction.DOWN_LEFT.value[0]][j + Direction.DOWN_LEFT.value[1]] == 'S'),
            (matrix[i + Direction.UP_LEFT.value[0]][j + Direction.UP_LEFT.value[1]] == 'S' and
                matrix[i + Direction.DOWN_RIGHT.value[0]][j + Direction.DOWN_RIGHT.value[1]] == 'M'),
            (matrix[i + Direction.UP_RIGHT.value[0]][j + Direction.UP_RIGHT.value[1]] == 'S' and
                matrix[i + Direction.DOWN_LEFT.value[0]][j + Direction.DOWN_LEFT.value[1]] == 'M')
        ]
        if sum(conditions) >= 2:
            print(f"X-MAS found at ({i}, {j}):")
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    print(matrix[i + di][j + dj], end=' ')
                print()
            return True
    return False

def part_two(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if is_x_mas(matrix, i, j):
                count += 1
    return count

if __name__ == "__main__":
    matrix = read_file()
    # res = part_one(matrix)
    res = part_two(matrix)
    print(res)