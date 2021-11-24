import codewars_test as test
import solution
import inspect
from random import randrange

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        prisoners = solution.gather_and_discuss()
        assertion = False
        for i in range(999999):
            if prisoners[i % 100].enter_room():
                assertion = True
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
                    "Prisoners should have two only attributes: a short string for the name and a small integer for the serial number.")
        test.expect(all(k in ('__module__', '__init__', '__dict__', '__weakref__', '__doc__') or callable(v) for k, v in vars(solution.Prisoner).items()),
                    'Prisoner should not have static properties')
        test.expect(isinstance(solution.light_bulb, bool),
                    'light_bulb should be a boolean')
        test.expect(all(d in ('Prisoner', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'gather_and_discuss', 'light_bulb') for d in dir(solution)),
                    'light_bulb, Prisoner and gather_and_discuss should be the only variables in the global environment')
        lines = inspect.getsource(solution)
        test.expect(lines.count('global') == lines.count('global light_bulb'),
                           'The solution code should use only one global variable for the light_bulb')
        test.expect(not lines.count('nonlocal'),
                           'The solution code should not use nonlocal variables')
        entered = [False for _ in range(100)]
        assertion = False
        for i in range(999999):
            r = randrange(100)
            entered[r] = True
            if i == 9:
                test.expect(all(isinstance(p, solution.Prisoner) for p in prisoners),
                            'gather_and_discuss should return a tuple of 100 prisoners')
                test.expect(all(k in ('__module__', '__init__', '__dict__', '__weakref__', '__doc__') or callable(v) for k, v in vars(solution.Prisoner).items()),
                            'Prisoner should not have static properties')
                test.expect(isinstance(solution.light_bulb, bool),
                            'light_bulb should be a boolean')
                test.expect(all(d in ('Prisoner', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'gather_and_discuss', 'light_bulb') for d in dir(solution)),
                            'light_bulb, Prisoner and gather_and_discuss should be the only variables in the global environment')
            if prisoners[r].enter_room():
                assertion = True
                test.expect(all(entered))
                break
        test.expect(assertion)

    @test.it("Random tests")
    def _():
        for _ in range(9):
            prisoners = solution.gather_and_discuss()
            for i in range(99):
                r = randrange(100)
                if prisoners[r].enter_room():
                    test.expect(False)
                    break
        for _ in range(9):
            prisoners = solution.gather_and_discuss()
            entered = [False for _ in range(100)]
            assertion = False
            for i in range(19999):
                r = randrange(100)
                entered[r] = True
                if prisoners[r].enter_room():
                    assertion = True
                    test.expect(all(entered))
                    break
            test.expect(assertion)
