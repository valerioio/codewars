import codewars_test as test
import solution
import inspect
from random import randrange

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        prisoners = solution.gather_and_discuss()
        light_bulb = False
        assertion = False
        for i in range(29200):
            light_bulb, assertion = prisoners[i % 100].enter_room(light_bulb)
            if assertion:
                test.expect(i >= 100)
                break
        test.expect(assertion)

@test.describe('Attempt tests')
def _():
    @test.it('Cheating tests')
    def _():
        prisoners = solution.gather_and_discuss()
        test.expect(isinstance(prisoners, tuple) and len(prisoners) == 100 and all(isinstance(p, solution.Prisoner) for p in prisoners),
                    'gather_and_discuss should return a tuple of 100 prisoners')
        test.expect(all(isinstance(v, str) and len(v)<1000 or isinstance(v, int) and v<1000 and len(vars(p)) <= 2 for p in prisoners for v in vars(p).values()),
                    "Prisoners should have two only attributes: a short string for the name and a small integer for the counter.")
        test.expect(all(k in ('__module__', '__init__', '__dict__', '__weakref__', '__doc__') or callable(v) for k, v in vars(solution.Prisoner).items()),
                    'Prisoner should not have static properties')
        test.expect(all(d in ('Prisoner', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'gather_and_discuss') for d in dir(solution)),
                    'Prisoner and gather_and_discuss should be the only variables in the global environment')
        lines = inspect.getsource(solution)
        test.expect(not lines.count('global') and not lines.count('nonlocal'),
                    'The solution code should not use global or nonlocal variables')
        light_bulb, assertion = prisoners[randrange(100)].enter_room(False)
        prisoners[randrange(100)].enter_room(light_bulb)
        test.expect(all(isinstance(p, solution.Prisoner) for p in prisoners),
                    'gather_and_discuss should return a tuple of 100 prisoners')
        test.expect(all(k in ('__module__', '__init__', '__dict__', '__weakref__', '__doc__') or callable(v) for k, v in vars(solution.Prisoner).items()),
                    'Prisoner should not have static properties')
        test.expect(all(d in ('Prisoner', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'gather_and_discuss') for d in dir(solution)),
                    'Prisoner and gather_and_discuss should be the only variables in the global environment')

    @test.it("Random tests")
    def _():
        for _ in range(9):
            prisoners = (solution.gather_and_discuss(), solution.gather_and_discuss())
            entered = ([False for _ in range(100)], [False for _ in range(100)])
            assertions = [False, False]
            light_bulbs = [False, False]
            b = randrange(1)
            for _ in range(0, 99999): # amount of days to be fixed
                r = randrange(100)
                entered[b][r] = True
                light_bulbs[b], assertions[b] = prisoners[b][r].enter_room(light_bulbs[b])
                if assertions[b]:
                    test.expect(all(entered[b]))
                    b ^= 1
                if not any(assertions):
                    b = randrange(1)
                if all(assertions):
                    break
            else:
                test.fail()
