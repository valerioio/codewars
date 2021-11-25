import codewars_test as test
import solution
from random import randrange

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        prisoners = [() for _ in range(100)]
        lightbulb = False
        assertion = False
        for i in range(29200):
            light_before = lightbulb
            lightbulb, assertion = solution.living_room(i % 100, lightbulb, prisoners[i % 100])
            prisoners[i % 100] = (*prisoners[i % 100], light_before)
            if assertion:
                test.expect(i >= 100,
                            'One of the prisoners made a false assertion')
                break
        test.expect(assertion,
                    'The prisoners waited too long to make an assertion')

@test.describe('Attempt tests')
def _():
    @test.it('Cheating tests')
    def _():
        prisoners = [() for _ in range(100)]
        lightbulb = False
        assertion = False
        for _ in range(29200):
            if not randrange(99) and not all(d in ('living_room', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__') for d in dir(solution)):
                test.fail('living_room should be the only name in the global scope')
            r = randrange(100)
            light_before = lightbulb
            lightbulb, assertion = solution.living_room(r, lightbulb, prisoners[r])
            if(not isinstance(lightbulb, bool) or not isinstance(assertion, bool)):
                test.fail('living_room should return to booleans')
            prisoners[r] = (*prisoners[r], light_before)
            if assertion:
                break

        for _ in range(9):
            prisoners = [() for _ in range(100)]
            lightbulb = False
            assertion = False
            skip = randrange(100)
            for _ in range(29200):
                r = randrange(100)
                if r == skip:
                    r = (r + 1) % 100
                light_before = lightbulb
                lightbulb, assertion = solution.living_room(r, lightbulb, prisoners[r])
                prisoners[r] = (*prisoners[r], light_before)
                if assertion:
                    test.fail('One of the prisoners made a false assertion')

        test.pass_()

    @test.it("Random tests")
    def _():
        for _ in range(9):
            prisoners = [[() for _ in range(100)], [() for _ in range(100)]]
            lightbulbs = [False, False]
            assertions = [False, False]
            entered = [[False for _ in range(100)], [False for _ in range(100)]]
            days = [0, 0]
            b = randrange(1)
            for _ in range(99999):
                r = randrange(100)
                light_before = lightbulbs[b]
                lightbulbs[b], assertions[b] = solution.living_room(r, lightbulbs[b], prisoners[b][r])
                prisoners[b][r] = (*prisoners[b][r], light_before)
                entered[b][r] = True
                days[b] += 1
                if assertions[b]:
                    test.expect(all(entered[b]),
                                'One of the prisoners made a false assertion')
                    b ^= 1
                if not any(assertions):
                    b = randrange(1)
                if all(assertions):
                    break
            test.expect(all(d < 29200 for d in days),
                        'The prisoners waited too long to make an assertion')
