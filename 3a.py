from pprint import pprint
import numpy as np
import string

sum=0

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


print(sum)