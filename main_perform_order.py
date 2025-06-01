#!/home/private/projects/pytest/demo/py-pytest/.env/bin/python3

import pytest

pytest.main(['-vsx', '-m', 'perform_order', '--repeat-scope=class', '--count=100'])