from pymodbus.client import ModbusTcpClient

host="192.168.31.30"

class GwMB:
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

    def read(self, slaveId:int=1)->list:
        if not self._connected:
            print("ModbusServer never connected")
            return []
        rr = self.client.read_input_registers(address=0, count=66, slave=slaveId)
        # for v in rr.registers:
        #     print(hex(v), end=" ")
        # print("\nlen:", len(rr.registers))
        return rr.registers

    def close(self):
        self.client.close()