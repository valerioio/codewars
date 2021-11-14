import codewars_test as test
from solution import to_mountain
from collections import defaultdict
from random import randint, randrange, shuffle

@test.describe("Example tests")
def _():
    @test.it("Fixed tests")
    def _():
        test.assert_equals(to_mountain([[1]]), [[1]])
        test.assert_equals(to_mountain([[1, 1]]), [[1, 1]])
        test.assert_equals(to_mountain([[1, 2]]), [[1, 2]])
        test.assert_equals(to_mountain([[1, 3]]), [[2, 3]])
        test.assert_equals(to_mountain([[2, 2, 1, 2], [1, 0, 2, 1], [1, 0, 1, 2], [1, 2, 2, 1]]), [[2, 2, 1, 2], [1, 1, 2, 1], [1, 1, 1, 2], [1, 2, 2, 1]])
        test.assert_equals(to_mountain([[2, 2, 1, 2], [1, 0, 2, 1], [1, 0, 1, 2], [1, 2, 2, 4]]), [[2, 2, 1, 2], [1, 2, 2, 2], [1, 2, 3, 3], [1, 2, 3, 4]])
        test.assert_equals(to_mountain([[2, 2, 1, 2], [1, 0, 2, 1], [1, 0, 4, 2], [1, 2, 2, 4]]), [[2, 2, 2, 2], [2, 3, 3, 3], [2, 3, 4, 3], [2, 3, 3, 4]])
        test.assert_equals(to_mountain([[1, 2, 4, 2], [3, 3, 3, 4], [1, 2, 4, 2], [4, 4, 1, 3]]), [[2, 3, 4, 3], [3, 3, 3, 4], [3, 3, 4, 3], [4, 4, 3, 3]])

@test.describe("Random tests")
def _():
    def check(input):
        expected = to_mountain_check(input)
        actual = to_mountain(input)
        test.assert_equals(actual, expected)

    def to_mountain_check(mat):
        mat = [[n for n in r] for r in mat]
        d = defaultdict(set)
        highest = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    d[mat[i][j]].add((i, j))
                    highest = max(highest, mat[i][j])
        directions = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j)
        while highest and d:
            x, y = d[highest].pop()
            if not d[highest]:
                d.pop(highest)
            for i, j in directions:
                xi, yj = x+i, y+j
                if 0<=xi<len(mat) and 0<=yj<len(mat[0]) and mat[xi][yj]<mat[x][y]-1:
                    if((xi, yj) in d[mat[xi][yj]]):
                        d[mat[xi][yj]].remove((xi, yj))
                        if not d[mat[xi][yj]]:
                            d.pop(mat[xi][yj])
                    mat[xi][yj] = mat[x][y]-1
                    d[mat[xi][yj]].add((xi, yj))
            while highest and d and highest not in d:
                highest -= 1
        return mat


    def random_mat(l, h, V):
        rows, cols = randint(l, h), randint(l, h)
        return [[randrange(V) for _ in range(cols)] for _ in range(rows)]

    def spray(l, h, V=100, N=5, D=9000):
        mat = random_mat(l, h, V)
        for _ in range(N):
            mat[randrange(len(mat))][randrange(len(mat[0]))] = D+randrange(200)
        return mat

    def creep(l, h, V):
        rows, cols = randint(l, h), randint(l, h)
        mat = [[i+j+randrange(V) for j in range(cols)] for i in range(rows)]
        if randrange(2): mat.reverse()
        if randrange(2): mat = [row[::-1] for row in mat]
        if randrange(2): mat = [*map(list, zip(*mat))]
        return mat

    @test.it("Easy tests")
    def _():
        tests = []
        n = 10
        tests.extend(random_mat(8, 12, 20) for _ in range(2*n))
        tests.extend(spray(8, 12, 10, 3, 30) for _ in range(n))
        tests.extend(creep(8, 12, 3) for _ in range(2*n))
        shuffle(tests)
        for matrix in tests:
            check(matrix)

    @test.it("Medium tests")
    def _():
        tests = []
        n = 10
        tests.extend(random_mat(30, 40, 100) for _ in range(n))
        tests.extend(spray(30, 40) for _ in range(n))
        tests.extend(creep(30, 40, 5) for _ in range(2*n))
        shuffle(tests)
        for matrix in tests:
            check(matrix)

    @test.it("Heavy tests")
    def _():
        tests = []
        n = 12
        tests.extend(random_mat(90,100,1000000000) for _ in range(n))
        tests.extend(spray(90, 100) for _ in range(n))
        tests.extend(creep(90, 100, 4) for _ in range(n))
        shuffle(tests)
        for matrix in tests:
            check(matrix)
