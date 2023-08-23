# [Traverse array elements diagonally | Codewars](https://www.codewars.com/kata/5968fb556875980bd900000f)
# 6 kyu
# Traverse array elements diagonally
#
# In this kata you're given an `n x n` array and you're expected to traverse the elements diagonally from the `bottom right` to the `top left`.
#
# Example
#
# ```
#   1 6 7
#   7 2 4
#   3 5 9
# ```
#
# your solution should return elements in the following order
#
# ```
# 9
# 4 5
# 7 2 3
# 6 7
# 1
# ```
#
# `//=> [9, 4, 5, 7, 2, 3, 6, 7, 1]`
#
# Your task is to write the function `diagonal()` that returns the array elements in the above manner.
#
# Another Example
#
# ```
# arr = [
#  [4, 5, 7],
#  [3, 9, 1],
#  [7, 6, 2]
# ]
#
# diagonal(arr) //=> [2, 1, 6, 7, 9, 7, 5, 3, 4]
# ```
#
# You can assume the test cases are well formed.
#
# `Arrays` `Logic` `Algorithms`

data = [
    [4, 5, 7],
    [3, 9, 1],
    [7, 6, 2]
]

# 2
# 1, 6
# 7, 9, 7
# 5, 3
# 4

# 2, 1, 6, 7, 9, 7, 5, 3, 4

#         2,2
#     1,2 2,1
# 0,2 1,1 2,0
# 0,1 1,0
# 0,0

# version colonne
# 2,2 2,1 2,0
# 1,2 1,1 1,0
# 0,2 0,1 0,0

# version diagonale
# 2,2 1,2 0,2
# 2,1 1,1 0,1
# 2,0 1,0 0,0

indexes = [[] for _ in range(5)]

row_base = 0

for y in range(2, -1, -1):
    row_offset = 0

    for x in range(2, -1, -1):
        indexes[row_base + row_offset].append((x, y))

        row_offset += 1

    row_base += 1

result = []

for row in indexes:
    for x, y in row:
        result.append(data[x][y])

print(result)
