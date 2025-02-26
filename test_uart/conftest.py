import pytest

@pytest.fixture(scope='module')
def uart_fixture_module() -> any :
    print("\n[ Gonna open uart ] ---------------")
    yield
    print("\n[ Close uart port ] ---------------")