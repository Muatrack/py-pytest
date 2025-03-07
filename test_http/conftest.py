import pytest
import requests
import responses_validator

@pytest.fixture(scope='module')
def http_fixture_module() -> any :
    print("\n[ Gonna open http ] ---------------")
    yield
    print("\n[ Close http conn ] ---------------")

# @pytest.fixture(scope='module')
def pytest_yaml_run_step(item):
    step = item.current_step
    request = step.get('request')
    response = step.get('response')

    if request:
        print(f'url={request["url"]}')
        item.resp = requests.request(**request)

    if response:
        responses_validator.validator(item.resp, **response)
