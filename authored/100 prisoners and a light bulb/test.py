import codewars_test as test
import solution
from random import randrange, shuffle

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        passed = True
        prisoners = [[] for _ in range(100)]
        lightbulb = False
        assertion = False
        for i in range(29200):
            light_before = lightbulb
            lightbulb, assertion = solution.living_room(i % 100, lightbulb, prisoners[i % 100])
            prisoners[i % 100].append(light_before)
            if assertion:
                passed = False
                test.expect(i >= 99,
                            'One of the prisoners made a false assertion')
                break
        if passed:
            test.expect(assertion,
                        'The prisoners waited too long to make an assertion')

@test.describe('Attempt tests')
def _():
    @test.it('Cheating tests')
    def _():
        passed = True
        message = ''
        prisoners = [[] for _ in range(100)]
        lightbulb = False
        assertion = False
        names_in_scope = ('living_room', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__')
        locals = '<locals>'
        if(solution.living_room.__code__.co_argcount != 3 or solution.living_room.__defaults__):
            passed = False
            message = 'living_room should take in exactly three arguments'
        for _ in range(29200):
            if not all(d in names_in_scope for d in dir(solution)):
                passed = False
                message = 'living_room should be the only name in the global scope'
            if vars(solution.living_room):
                passed = False
                message = 'living_room should not have attributes'
            if locals in str(vars(solution)['living_room']):
                passed = False
                message = 'living_room should not be a closure'
            r = randrange(100)
            light_before = lightbulb
            lightbulb, assertion = solution.living_room(r, lightbulb, prisoners[r])
            prisoners[r].append(light_before)
            if(not isinstance(lightbulb, bool) or not isinstance(assertion, bool)):
                passed = False
                message = 'living_room should return two booleans'
            if assertion:
                break
        if passed:
            test.pass_()
        else:
            test.fail(message)

    bonus = True
    @test.it("Random tests")
    def _():
        cheating = True
        for _ in range(9):
            passed = True
            prisoners = [[] for _ in range(100)]
            lightbulb = False
            assertion = False
            for _ in range(29200):
                r = randrange(100)
                light_before = lightbulb
                lightbulb, assertion = solution.living_room(r, lightbulb, prisoners[r])
                prisoners[r].append(light_before)
                if assertion:
                    passed = all(prisoners)
                    cheating = cheating and passed
                    test.expect(passed,
                                'One of the prisoners made a false assertion')
                    break
            if passed:
                cheating = cheating and assertion
                test.expect(assertion,
                'The prisoners waited too long to make an assertion')
        bonus = not cheating

        def skip():
            passed = True
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
                    passed = False
                    test.fail('One of the prisoners made a false assertion. (This might be caused by using state)')
                    break
            if passed:
                test.pass_()

        def simultaneous():
            passed = [True, True]
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
                    passed[b] = False
                    test.expect(all(prisoners[b]),
                                'One of the prisoners made a false assertion. (This might be caused by using state)')
                    b ^= 1
                if not any(assertions):
                    b = randrange(2)
                if all(assertions):
                    break
            for b in range(2):
                if passed[b]:
                    test.expect(days[b] < 29200,
                    'The prisoners waited too long to make an assertion. (This might be caused by using state)')

        if cheating:
            tests = [skip, simultaneous]
            random_b = [0] * 9 + [1] * 9
            shuffle(random_b)
            for b in random_b:
                tests[b]()

    if bonus:
        for _ in range(9):
            prisoners = [[] for _ in range(100)]
            lightbulb = bool(randrange(2))
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
                    bonus = False
                    break
    if bonus:
        @test.it("Bonus points!")
        def _():
            test.pass_()
    else:
        @test.it("<span style='color:red'>No bonus points...</span>")
        def _():
            pass
