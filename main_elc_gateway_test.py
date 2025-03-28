#!/home/private/projects/pytest/demo/py-pytest/.env/bin/python3

import pytest

pytest.main(['-s', '-m', 'http_api_elc_gateway', "--count=10"])