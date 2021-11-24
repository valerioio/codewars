import codewars_test as test
from solution import gather_and_discuss

@test.describe('Example tests')
def _():
    @test.it('Fixed test')
    def _():
        prisoners = gather_and_discuss()
        assertion = False
        for i in range(999999):
            if prisoners[i % 100].enter_room():
                assertion = True
                test.expect(i >= 100)
                break
        test.expect(assertion)
