import pytest
import requests
# import responses_validator
import time

# @pytest.mark.repeat(10)
def test_http_ws_api_server():
    time.sleep(2)
    resp = requests.get('http://192.168.20.1/server', headers={'ookie': 'auth_key=Basic ZXNwMzI6NjY2ODg4'}, timeout=3)
    print("Response content len:", len(resp.content), '\n')
    assert resp.status_code==200