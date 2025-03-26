#!/home/disk-data/projects/pytest/demo/py-pytest/.env/bin/python
import pytest

pytest.main(['-s', '-m', 'http_api_elc_gateway', "--count=10"])