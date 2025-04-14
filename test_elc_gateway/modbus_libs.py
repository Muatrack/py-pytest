from pymodbus.client import ModbusTcpClient

host="192.168.30.31"

class GwMB:
    def connect(self, host:str="192.168.30.31", port:int=502)->bool:
        self.host = host
        self.client = ModbusTcpClient(host=host, port=port)
        bRet = self.client.connect()
        if bRet:
            self._connected = True
        else:
            self._connected = False

    def read(self, slaveId:int=1)->tuple:
        if not self._connected:
            print("ModbusServer never connected")
            return ()
        
        mbRespPDU = self.client.read_input_registers(address=0, count=66, slave=slaveId)
        return ()