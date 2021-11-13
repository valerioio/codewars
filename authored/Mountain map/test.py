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

def random_mat(m, l, h):
    r, c = randint(l, h), randint(l, h)
    return [[randint(0, m) for i in range(c)] for j in range(r)]
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
            random = random_mat(9, 49, 99)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = random_mat(99, 49, 99)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = random_mat(4, 49, 99)
            for h in range(randint(1, 9)):
                for j in range(len(random)):
                    for k in range(len(random[0])):
                        random[j][k] = randint(1, 19)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = random_mat(2, 79, 99)
            for h in range(randint(1, 2)):
                for j in range(len(random)):
                    for k in range(len(random[0])):
                        random[j][k] = randint(29, 99)
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            random = list(range(9801))
            shuffle(random)
            random = [random[i:i+99] for i in range(0, len(random), 99)]
            act(to_mountain(copy_of(random)), to_mountain_check(random))
            n = randint(0, 99)
            random = [[n+i+99*j for i in range(99)] for j in range(99)]
            act(to_mountain(copy_of(random)), to_mountain_check(random))
