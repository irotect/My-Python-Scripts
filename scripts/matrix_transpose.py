"""
Transposes the given matrix in the form of 2-d list.

ex. [[1,2,3],[4,5,6]] --> [[1, 4], [2, 5], [3, 6]]
"""
__script_name__ = "Matrix Transposer"
__version__ = "0.1.0"
__author__ = "Mayank Thakur"
__date__ = "17-01-2019"


def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        entry = []
        for row in matrix:
            entry.append(row[i])
        result.append(entry)
    return result


if __name__ == "__main__":
    m = [[1,2,3],[4,5,6]]
    n = [[1,4,9]]
    transposed_list = transpose(m)
    print(transposed_list)
