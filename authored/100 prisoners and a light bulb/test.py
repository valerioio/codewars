import codewars_test as test
import solution
from random import randrange

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        prisoners = [[] for _ in range(100)]
        lightbulb = False
        assertion = False
        for i in range(29200):
            light_before = lightbulb
            lightbulb, assertion = solution.living_room(i % 100, lightbulb, prisoners[i % 100])
            prisoners[i % 100].append(light_before)
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
        prisoners = [[] for _ in range(100)]
        lightbulb = False
        assertion = False
        names_in_scope = ('living_room', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__')
        locals = '<locals>'
        for _ in range(29200):
            if not all(d in names_in_scope for d in dir(solution)):
                test.fail('living_room should be the only name in the global scope')
            if locals in str(vars(solution)['living_room']):
                test.fail('living_room should not be a closure')
            r = randrange(100)
            light_before = lightbulb
            lightbulb, assertion = solution.living_room(r, lightbulb, prisoners[r])
            prisoners[r].append(light_before)
            if(not isinstance(lightbulb, bool) or not isinstance(assertion, bool)):
                test.fail('living_room should return two booleans')
            if assertion:
                break

        for _ in range(9):
            prisoners = [[] for _ in range(100)]
            lightbulb = False
            assertion = False
            skip = randrange(100)
            for _ in range(29200):
                r = randrange(100)
                light_before = lightbulb
                light_and_assertion = solution.living_room(r, lightbulb, prisoners[r])
                if r != skip:
                    lightbulb, assertion = light_and_assertion
                    prisoners[r].append(light_before)
                if assertion:
                    test.fail('One of the prisoners made a false assertion')
                    break

        test.pass_()

    @test.it("Random tests")
    def _():
        for _ in range(9):
            prisoners = [[[] for _ in range(100)], [[] for _ in range(100)]]
            lightbulbs = [False, False]
            assertions = [False, False]
            days = [0, 0]
            b = randrange(2)
            for _ in range(99999):
                r = randrange(100)
                light_before = lightbulbs[b]
                lightbulbs[b], assertions[b] = solution.living_room(r, lightbulbs[b], prisoners[b][r])
                prisoners[b][r].append(light_before)
                days[b] += 1
                if assertions[b]:
                    test.expect((all(p) for p in prisoners),
                                'One of the prisoners made a false assertion')
                    b ^= 1
                if not any(assertions):
                    b = randrange(2)
                if all(assertions):
                    break
            test.expect(all(d < 29200 for d in days),
                        'The prisoners waited too long to make an assertion')
