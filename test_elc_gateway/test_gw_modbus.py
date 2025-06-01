import pytest
import time
import modbus_libs as mb

host= "192.168.31.110"
port= 502
gmbClient = None
interval_ts:int = 0.1

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
        # time.sleep(interval_ts)

@pytest.mark.http_api_elc_gateway_modbus
class TestModbusAccess():

    
    def test_modbus_tcp_access_slv1(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(1, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:1")
        assert len(rr)==66

    def test_modbus_tcp_access_slv2(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(2, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:2")
        assert len(rr)==66

    def test_modbus_tcp_access_slv3(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(3, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:3")
        assert len(rr)==66

    def test_modbus_tcp_access_slv4(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(4, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:4")
        assert len(rr)==66

    def test_modbus_tcp_access_slv5(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(5, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:5")
        assert len(rr)==66

    def test_modbus_tcp_access_slv6(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(6, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:6")
        assert len(rr)==66

    def test_modbus_tcp_access_slv7(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(7, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:7")
        assert len(rr)==66 

    def test_modbus_tcp_access_slv8(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(8, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:8")
        assert len(rr)==66

    def test_modbus_tcp_access_slv9(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(9, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:9")
        assert len(rr)==66

    def test_modbus_tcp_access_slv10(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(10, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:10")
        assert len(rr)==66

    def test_modbus_tcp_access_slv11(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(11, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:11")
        assert len(rr)==66

    def test_modbus_tcp_access_slv12(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(12, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:12")
        assert len(rr)==66

    def test_modbus_tcp_access_slv13(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(13, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:13")
        assert len(rr)==66

    def test_modbus_tcp_access_slv14(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(14, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:14")
        assert len(rr)==66

    def test_modbus_tcp_access_slv15(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(15, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:15")
        assert len(rr)==66

    def test_modbus_tcp_access_slv16(self):
        '''
            测试modbus-tcp可访问性
        '''
        global gmbClient
        rr = gmbClient.read(16, 0, 66)
        # time.sleep(interval_ts)
        print("slvId:16")
        assert len(rr)==66
