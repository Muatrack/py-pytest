#!/home/private/projects/pytest/demo/py-pytest/.env/bin/python3

import pytest

pytest.main(['-svx', '-m', 'http_api_itower_controller', "--count=1"])