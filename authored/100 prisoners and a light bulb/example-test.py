import codewars_test as test
from solution import living_room

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
            lightbulb, assertion = living_room(i % 100, lightbulb, prisoners[i % 100])
            prisoners[i % 100].append(light_before)
            if assertion:
                passed = False
                test.expect(i >= 99, 'One of the prisoners made a false assertion')
                break
        if passed:
            test.expect(assertion, 'The prisoners waited too long to make an assertion')
