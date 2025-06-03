from pymodbus.client import ModbusTcpClient

class _GwMB:
    def connect(self, host:str="192.168.31.30", port:int=502)->bool:
        self.host = host
        self.client = ModbusTcpClient(host=host)
        bRet = self.client.connect()
        if bRet:
            self._connected = True
            print("Succ to connect")
        else:
            self._connected = False
            print("Fail to connect")

    def read(self, slaveId:int=1, regAddr:int=0, regCounts:int=66)->list:
        if not self._connected:
            print("ModbusServer never connected")
            return []
        rr = self.client.read_input_registers(address=regAddr, count=regCounts, slave=slaveId)
        return rr.registers

    def close(self):
        self.client.close()

_client = _GwMB()

def client_get():
    return _client
