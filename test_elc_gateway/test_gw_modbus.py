import pytest
import time
import modbus_libs as mb

@pytest.fixture(scope='module', autouse=True)
def modbus_options():
    print("\n[ modbus_options before yeild ]")
    yield
    print("\n[ modbus_options after yeild ]")

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access():
    '''
        测试modbus-tcp可访问性
    '''

    mbClient = mb.GwMB()
    mbClient.connect()
    time.sleep(3)
    rr:list = mbClient.read(1)
    mbClient.close()
    assert len(rr)==66