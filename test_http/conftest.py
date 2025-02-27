import pytest
import requests
import responses_validator

@pytest.fixture(scope='module')
def http_fixture_module() -> any :
    print("\n[ Gonna open http ] ---------------")
    yield
    print("\n[ Close http conn ] ---------------")

@pytest.mark.elcgw
@pytest.mark.usefixtures('http_fixture_module')
def pytest_yaml_run_step(item):
    print("\nyaml item:", item)
    step = item.current_step
    print("yaml steps:", step)
    request = step.get('request')
    response = step.get('response')

    if request:
        print(f'url={request["url"]}')
        item.resp = requests.request(**request)

    if response:
        print("got responses :\n", item.resp)
        responses_validator.validator(item.resp, **response)
        # responses_validator.validator(item.resp, status_code=200, text='*ws_state*')

    return True