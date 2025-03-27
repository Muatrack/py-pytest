#!/home/disk-data/projects/pytest/demo/py-pytest/.env/bin/python
import pytest

pytest.main(['-s', '-m', 'http_api_itower_controller', "--count=10"])