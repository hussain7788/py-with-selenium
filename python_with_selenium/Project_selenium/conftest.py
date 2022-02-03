import pytest

def pytest_addoption(parser):
    parser.addoption("--offset", action="store", default = 1)

@pytest.fixture(scope='session')
def offset(request):
    offset_value = request.config.option.offset
    if offset_value is None:
        pytest.skip()
    return offset_value
