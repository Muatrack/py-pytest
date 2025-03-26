import pytest
import requests
# import responses_validator
import time

httpd_header={'ookie': 'auth_key=Basic ZXNwMzI6NjY2ODg4'}

def blm_discovery_start():
    resp = requests.post('http://192.168.1.150/v1/api/slave', headers=httpd_header, data='{"action": "discst","params": {}}' ,timeout=1)
    # print("Response content len:", len(resp.content), '\n')
    assert resp.status_code==200

def blm_discovery_list():
    resp = requests.get('http://192.168.1.150/v1/api/slave/?id=240', timeout=3)
    # print("Response content len:", len(resp.content), '\n')
    assert resp.status_code==200

# @pytest.mark.repeat(10)
@pytest.mark.http_api_elc_gateway
def test_http_ws_api_server():
    time.sleep(1)
    blm_discovery_start()
    time.sleep(1)
    blm_discovery_list()