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

@test.describe("Solution tests")
def sol_test():
    def act(input):
        actual = to_mountain(copy_of(input))
        expected = to_mountain_check(copy_of(input))
        test.assert_equals(actual, expected, f"input: str(input)" if len(input)<10 else None)

    @test.it("Fixed tests")
    def fixed_tests():
        act([[1]])
        act([[1, 1]])
        act([[1, 2]])
        act([[1, 3]])
        act([[2, 2, 1, 2],[1, 0, 2, 1],[1, 0, 1, 2],[1, 2, 2, 1]])
        act([[2, 2, 1, 2],[1, 0, 2, 1],[1, 0, 1, 2],[1, 2, 2, 4]])
        act([[2, 2, 1, 2],[1, 0, 2, 1],[1, 0, 4, 2],[1, 2, 2, 4]])
        act([[1, 2, 4, 2],[3, 3, 3, 4],[1, 2, 4, 2],[4, 4, 1, 3]])

    @test.it("Random tests of small matrices (between 4 x 4 and 9 x 9) and small numbers (0 to 9)")
    def random_test():
        for i in range(9):
            act(random_mat(4, 4, 9))
            act(random_mat(9, 4, 9))

    @test.it("Random tests of big matrices (up to 99 x 99) and medium numbers (0 to 99)")
    def random_test():
        for i in range(9):
            act(random_mat(9, 89, 99))
            act(random_mat(99, 89, 99))

    @test.it("Random tests of big matrices (up to 99 x 99) and big numbers (up to 9999)")
    def random_test():
        for i in range(9):
            act(random_mat(9999, 89, 99))

    @test.it("Random tests of big matrices and all the numbers between 0 and 9801 shuffled")
    def random_test():
        for i in range(9):
            random = list(range(9801))
            shuffle(random)
            random = [random[i:i+99] for i in range(0, len(random), 99)]
            act(random)

    @test.it("Random tests of big matrices and all different numbers in increasing order")
    def random_test():
        for i in range(9):
            n = randint(0, 99)
            random = [[n+i+99*j for i in range(99)] for j in range(99)]
            act(random)

#     @test.it("Random tests of big matrices with many small numbers and few medium numbers")
#     def random_test():
#         for i in range(4):
#             random = random_mat(9, 79, 99)
#             for h in range(randint(1, 9)):
#                 for j in range(len(random)):
#                     for k in range(len(random[0])):
#                         random[j][k] = randint(1, 19)
#             act(random)

#     @test.it("Random tests of big matrices with many small numbers and few big numbers")
#     def random_test():
#         for i in range(4):
#             random = random_mat(9, 79, 99)
#             for h in range(randint(1, 2)):
#                 for j in range(len(random)):
#                     for k in range(len(random[0])):
#                         random[j][k] = randint(79, 99)
#             act(random)
