import pytest

@pytest.mark.utc2
@pytest.mark.parametrize("v1, v2", [(2,3), (1,4), (2,3)])
class Test_Sample2():

    def test_1(self, v1, v2):
        assert v1 + v2 == 5
