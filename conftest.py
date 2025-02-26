import pytest

@pytest.fixture(scope='package')
def env_fixture_package() -> any :
    print("\n[ Prepare environment of testcases ] ---------------")
    yield
    print("\n[ Clear environment of testcases] ---------------")