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

#@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    for sId in range(1,17):
        rr = gmbClient.read(sId, 0, 66)
        assert len(rr)==66
        time.sleep(0.5)

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv1():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(1, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv2():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(2, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv3():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(3, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv4():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(4, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv5():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(5, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv6():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(6, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv7():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(7, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66 

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv8():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(8, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv9():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(9, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv10():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(10, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv11():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(11, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv12():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(12, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv12():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(13, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv14():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(14, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv15():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(15, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66

@pytest.mark.http_api_elc_gateway_modbus
def test_modbus_tcp_access_slv16():
    '''
        测试modbus-tcp可访问性
    '''
    global gmbClient
    rr = gmbClient.read(16, 0, 66)
    time.sleep(0.5)
    assert len(rr)==66