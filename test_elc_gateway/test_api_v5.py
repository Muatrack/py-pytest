import pytest
import requests
import time
import http_api_libs as gw

httpd_header={'ookie': 'auth_key=Basic ZXNwMzI6NjY2ODg4'}

def gw_server_get():
    resp = gw.http_api_server_get()

# @pytest.mark.repeat(10)
@pytest.mark.http_api_elc_gateway
def test_http_gw_accessable():
    '''
        网关访问性
    '''

    time.sleep(1)
    gw_server_get()

@pytest.mark.http_api_elc_gateway
def test_modbus_tcp_access():
    '''
        测试modbus-tcp可访问性
    '''

    