#!/home/private/projects/pytest/demo/py-pytest/.env/bin/python3

import pytest

pytest.main(['-m', 'http_api_elc_gateway_modbus', "--count=1000"])