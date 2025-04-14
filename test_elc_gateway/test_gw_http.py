import pytest
import time
import http_api_libs as gw

def gw_server_get():
    resp = gw.http_api_server_get()

# @pytest.mark.repeat(10)
@pytest.mark.http_api_elc_gateway_http
def test_http_gw_accessable():
    '''
        网关访问性
    '''

    time.sleep(1)
    gw_server_get()