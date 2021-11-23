import codewars_test as test
from solution import to_be_flipped
from heapq import heapify, heappop, heappush
from random import randint, randrange, shuffle

@test.describe("Example tests")
def _():
    @test.it("Fixed tests")
    def _():
        test.assert_equals(to_be_flipped([[0]]), 0)
        test.assert_equals(to_be_flipped([[1]]), 1)
        test.assert_equals(to_be_flipped([[0, 1]]), 1)
        test.assert_equals(to_be_flipped([[1, 1], [1, 1]]), 3)
        test.assert_equals(to_be_flipped([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 1)
        test.assert_equals(to_be_flipped([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]), 4)
        test.assert_equals(to_be_flipped([[0, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]), 2)
        test.assert_equals(to_be_flipped([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]), 4)
        test.assert_equals(to_be_flipped([[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]), 0)

@test.describe("Random tests")
def _():
    def check(input):
        expected = to_be_flipped_check(input)
        actual = to_be_flipped(input)
        test.assert_equals(actual, expected)

    def to_be_flipped_check(mat):
        ori = [[n for n in r] for r in mat]
        mat = [[n and 10001 for n in r] for r in mat]
        mat[0][0] = 1
        queue = [(1, 0, 0)]
        heapify(queue)
        directions = ((1, 0), (0, 1), (0, -1), (-1, 0))
        while not mat[-1][-1] or mat[-1][-1]>queue[0][0]:
            _, x, y = heappop(queue)
            for i, j in directions:
                xi, yj = x+i, y+j
                if 0<=xi<len(mat) and 0<=yj<len(mat[0]):
                    if not mat[xi][yj] or mat[x][y]+ori[xi][yj]<mat[xi][yj]:
                        mat[xi][yj] = mat[x][y]+ori[xi][yj]
                        heappush(queue, (mat[xi][yj], xi, yj))
        return mat[-1][-1] - (not ori[0][0])

    X = 60

    def random_mat(l, h, p=1/2):
        rows, cols = randint(l, h), randint(l, h)
        k = int(p*X)
        return [[int(randrange(X)<k) for _ in range(cols)] for _ in range(rows)]

    def snakes(l, h):
        rows, cols = randint(l, h), randint(l, h)
        mat = [[1 for _ in range(cols)] for _ in range(rows)]
        s = (rows+cols)//2 or 1
        n = rows*cols//(2*s)
        dir = ((1, 0), (0, 1), (0, -1), (-1, 0))
        for _ in range(n):
            x, y = randrange(cols), randrange(rows)
            for _ in range(s):
                mat[y][x] = 0
                i, j = dir[randrange(4)]
                x, y = x+i, y+j
                if not(0<=x<len(mat[0]) and 0<=y<len(mat)):
                    x, y = x-i, y-j
        return mat

    def checkers(l, h):
        rows, cols = randint(l, h), randint(l, h)
        k = 9*X//10
        return [[int(randrange(X)<k)^((i+j)%2) for i in range(cols)] for j in range(rows)]

    @test.it("Easy tests")
    def _():
        tests = []
        n = 10
        l, h = 1, 9
        tests.extend(random_mat(l, h, i/X) for i in range(X-1, 0, -X//n))
        tests.extend(snakes(l, h) for _ in range(n//2))
        tests.extend(checkers(l, h) for _ in range(n//2))
        shuffle(tests)
        for matrix in tests:
            check(matrix)

    @test.it("Medium tests")
    def _():
        tests = []
        n = 10
        l, h = 19, 29
        tests.extend(random_mat(l, h, i/X) for i in range(X-1, 0, -X//n))
        tests.extend(snakes(l, h) for _ in range(n//2))
        tests.extend(checkers(l, h) for _ in range(n//2))
        shuffle(tests)
        for matrix in tests:
            check(matrix)

    @test.it("Heavy tests")
    def _():
        tests = []
        n = 10
        l, h = 89, 99
        tests.extend(random_mat(l, h, i/X) for i in range(X-1, 0, -X//n))
        tests.extend(snakes(l, h) for _ in range(n//2))
        tests.extend(checkers(l, h) for _ in range(n//2))
        shuffle(tests)
        for matrix in tests:
            check(matrix)

    @test.it("Heavier tests")
    def _():
        tests = []
        n = 10
        l, h = 189, 199
        tests.extend(random_mat(l, h, i/X) for i in range(X-1, 0, -X//n))
        tests.extend(snakes(l, h) for _ in range(n//2))
        tests.extend(checkers(l, h) for _ in range(n//2))
        shuffle(tests)
        for matrix in tests:
            check(matrix)
