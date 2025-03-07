import pytest

@pytest.mark.usefixtures('env_fixture_package')
@pytest.mark.usefixtures('http_fixture_module')
@pytest.mark.api
def test_http_v1():
    pass