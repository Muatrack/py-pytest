#!/home/private/projects/pytest/demo/py-pytest/.env/bin/python3

import pytest
import sys

sys.stdout("/tmp/t.log", "w")
sys.stderr = sys.stdout
pytest.main(['-m', 'http_api_elc_gateway_modbus', '--repeat-scope=class', "--count=10000"])
# pytest.main(['-vs', '-m', 'http_api_elc_gateway_modbus', '--repeat-scope=class', "--count=1000"])
# pytest.main(['-xvs', '-m', 'http_api_elc_gateway_modbus', '--repeat-scope=class', "--count=1000"])