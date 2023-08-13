def sum_all_cross(matrix):
    """
    Sum all cross direction of matrix.
    matrix: input integer value in list.
    """
    sum = sum_cross(matrix)
    reversed_matrix = list(reversed(matrix))
    sum += sum_cross(reversed_matrix)
    return sum


def sum_cross(matrix):
    """
    Sum matrix in one cross direction.
    matrix: input integer value in list.
    """
    target_index = 0
    sum = 0
    for row in matrix:
        sum += row[target_index]
        target_index +=1
    return sum
    

if __name__=='__main__':
    """
    Calculate two cross direction of matrix.
    e.g. (1+5+9) + (3+5+7)
    """
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    result = sum_all_cross(matrix)
    print(result)