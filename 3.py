from pprint import pprint
import numpy as np
import string

def init_matrix():
    matrix=[]
    row=[]

    with open("3_input.txt") as f:
        while True:
            char = f.read(1)

            if not char:
                break

            if char == '\n':
                matrix.append(row)
                row=[]
                continue

            row.append(char)

    matrix=np.array(matrix, dtype=str)
    return matrix

def part_one(matrix):
    sum=0
    is_picked=np.zeros(matrix.shape, dtype=int)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] in string.punctuation and not matrix[i, j] == '.':
                if i<is_picked.shape[0]:
                    is_picked[i+1, j] = True
                if i>0:
                    is_picked[i-1, j] = True
                if j<is_picked.shape[1]:
                    is_picked[i, j+1] = True
                if j>0:
                    is_picked[i, j-1] = True
                if i<is_picked.shape[0] and j<is_picked.shape[1]:
                    is_picked[i+1, j+1] = True
                if i>0 and j>0:
                    is_picked[i-1, j-1] = True
                if i<is_picked.shape[0] and j>0:
                    is_picked[i+1, j-1] = True
                if i>0 and j<is_picked.shape[1]:
                    is_picked[i-1, j+1] = True

    temp=''
    for i in range(is_picked.shape[0]):
        cols = iter(range(is_picked.shape[1]))
        for j in cols:
            if is_picked[i, j] == 1 and matrix[i, j] in string.digits:
                temp+=matrix[i,j]

                k=1
                while j-k>=0 and matrix[i, j-k] in string.digits: # back
                    temp=matrix[i, j-k]+temp
                    k+=1

                k=1
                while j+k<matrix.shape[1] and matrix[i, j+k] in string.digits: # forward
                    temp=temp+matrix[i, j+k]
                    k+=1
                for skip in range(k-1):
                    next(cols)

                sum+=int(temp)
                temp=''

    return sum

def part_two(matrix):
    sum=0
    is_picked=[[[] for j in range(matrix.shape[1])] for i in range(matrix.shape[0])]

    counter=1
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == '*':
                if i<len(is_picked):
                    is_picked[i+1][j].append(counter)
                if i>0:
                    is_picked[i-1][j].append(counter)
                if j<len(is_picked[0]):
                    is_picked[i][j+1].append(counter)
                if j>0:
                    is_picked[i][j-1].append(counter)
                if i<len(is_picked) and j<len(is_picked[0]):
                    is_picked[i+1][j+1].append(counter)
                if i>0 and j>0:
                    is_picked[i-1][j-1].append(counter)
                if i<len(is_picked) and j>0:
                    is_picked[i+1][j-1].append(counter)
                if i>0 and j<len(is_picked[0]):
                    is_picked[i-1][j+1].append(counter)
                counter+=1

    temp=''
    gear_mult=1
    gear_found=0
    for c in range(1, counter):
        for i in range(len(is_picked)):
            cols = iter(range(len(is_picked[0])))
            for j in cols:
                if c in is_picked[i][j] and matrix[i][j] in string.digits:
                    temp+=matrix[i][j]

                    k=1
                    while j-k>=0 and matrix[i][j-k] in string.digits: # back
                        temp=matrix[i][j-k]+temp
                        k+=1

                    k=1
                    while j+k<matrix.shape[0] and matrix[i][j+k] in string.digits: # forward
                        temp=temp+matrix[i][j+k]
                        k+=1
                    for skip in range(k-1):
                        next(cols)

                    # print(temp, c)
                    gear_found+=1
                    gear_mult*=int(temp)
                    temp=''

        if gear_found == 2: # or >=2 ?, unclear but not in my dataset
            sum+=gear_mult
            # print("sum->", sum)
        gear_found=0
        gear_mult=1

    return sum


if __name__ == "__main__":
    matrix=init_matrix()
    # sum=part_one(matrix)
    sum=part_two(matrix)
    print(sum)