import codewars_test as test
from solution import gather_and_discuss

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        prisoners = gather_and_discuss()
        light_bulb = False
        assertion = False
        for i in range(29200):
            light_bulb, assertion = prisoners[i % 100].enter_room(light_bulb)
            if assertion:
                test.expect(i >= 100)
                break
        test.expect(assertion)
