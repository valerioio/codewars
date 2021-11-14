import codewars_test as test
from collections import defaultdict
from itertools import product
from random import randint, shuffle

def to_mountain_check(mat):
    d = defaultdict(set)
    highest = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]:
                d[mat[i][j]].add((i, j))
                highest = max(highest, mat[i][j])
    directions = list(product((-1, 0, 1), (-1, 0, 1)))
    directions.pop(4)
    while highest:
        x, y = d[highest].pop()
        for i, j in directions:
            xi, yj = x+i, y+j
            if 0<=xi<len(mat) and 0<=yj<len(mat[0]) and mat[xi][yj]<mat[x][y]-1:
                if((xi, yj) in d[mat[xi][yj]]):
                    d[mat[xi][yj]].remove((xi, yj))
                mat[xi][yj] = mat[x][y]-1
                d[mat[xi][yj]].add((xi, yj))
        while highest and not d[highest]:
            highest -= 1
    return mat

def random_mat(max_height, min_size, max_size):
    rows, cols = randint(min_size, max_size), randint(min_size, max_size)
    return [[randint(0, max_height) for i in range(cols)] for j in range(rows)]
def copy_of(m):
    return [[n for n in r] for r in m]

@test.describe("Solution test")
def sol_test():
    def act(matrix, expected):
        actual = to_mountain(matrix)
        test.assert_equals(actual, expected, str(matrix))

    @test.it("Fixed tests")
    def fixed_tests():
        act([[1]], [[1]])
        act([[1, 1]], [[1, 1]])
        act([[1, 2]], [[1, 2]])
        act([[1, 3]], [[2, 3]])
        act([[2, 2, 1, 2],
             [1, 0, 2, 1],
             [1, 0, 1, 2],
             [1, 2, 2, 1]],
            [[2, 2, 1, 2],
             [1, 1, 2, 1],
             [1, 1, 1, 2],
             [1, 2, 2, 1]])
        act([[2, 2, 1, 2],
             [1, 0, 2, 1],
             [1, 0, 1, 2],
             [1, 2, 2, 4]],
            [[2, 2, 1, 2],
             [1, 2, 2, 2],
             [1, 2, 3, 3],
             [1, 2, 3, 4]])
        act([[2, 2, 1, 2],
             [1, 0, 2, 1],
             [1, 0, 4, 2],
             [1, 2, 2, 4]],
            [[2, 2, 2, 2],
             [2, 3, 3, 3],
             [2, 3, 4, 3],
             [2, 3, 3, 4]])
        act([[1, 2, 4, 2],
             [3, 3, 3, 4],
             [1, 2, 4, 2],
             [4, 4, 1, 3]],
            [[2, 3, 4, 3],
             [3, 3, 3, 4],
             [3, 3, 4, 3],
             [4, 4, 3, 3]])

    @test.it("Random tests")
    def random_test():
        for i in range(9):
            random = random_mat(2, 4, 9)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = random_mat(9, 89, 99)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = random_mat(99, 89, 99)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = random_mat(9999, 89, 99)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
