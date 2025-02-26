import pytest
import requests
import responses_validator

@pytest.fixture(scope='module')
def uart_fixture_module() -> any :
    print("\n[ Gonna open uart ] ---------------")
    yield
    print("\n[ Close uart port ] ---------------")


def pytest_yaml_run_step(item):
    print("\nxxxxxxxxxxxxxxxxx Yaml testcases xxxxxxxxxxxxxxxx ")
    step = item.current_step
    request = step.get('request')
    response = step.get('response')

    if request:
        print(f'url={request["url"]}')
        item.resp = requests.request(**request)

    if response:
        responses_validator.validator(item.resp, **response)

    return True