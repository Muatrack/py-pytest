import pytest

@pytest.fixture(scope='module')
def http_fixture_module() -> any :
    print("\n[ Gonna open http connection ] ---------------")
    yield
    print("\n[ Close http connection ] ---------------")