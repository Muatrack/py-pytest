import pytest

@pytest.fixture(scope='module')
def uart_fixture_module() -> any :
    print("\n[ Gonna open uart ] ---------------")
    yield
    print("\n[ Close uart port ] ---------------")


def pytest_yaml_run_step(item):
    print("Yaml testcases ... ")