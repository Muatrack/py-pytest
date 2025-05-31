import pytest
import time
import modbus_libs as mb

host= "192.168.1.108"
port= 502
gmbClient = None

@pytest.fixture(scope='module', autouse=True)
def modbus_options():
    global host
    print("\n[ modbus_options before yeild ]")

    global gmbClient
    gmbClient = mb.client_get()
    gmbClient.connect(host=host)

    yield
    
    print("\n[ modbus_options after yeild ]")
    mb.client_get().close()

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(1)
    time.sleep(0.2)
    assert len(rr)==66
