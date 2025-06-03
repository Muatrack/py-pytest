
import math
import components.modbus.modbus_tcp_libs as mb

host = '192.168.31.110'
gmbClient = 0
def modbus_tcp_access_loop(host:str=''):
        global gmbClient
        gmbClient.connect(host=host)
        for slvId in range(1, 128):
                rr = gmbClient.read(slvId, 0, 66)                
                if len(rr) !=66: 
                        print(f"slvId:{slvId}, got empty responses")
                        continue
                mcuTemp:int = int(rr[2]); mcuTemp=math.floor(mcuTemp / 1000)
                if mcuTemp != 3: print(f"slvId:{slvId}, mcu temp:{mcuTemp} ({rr[2]})")
                freq:int = int(rr[3]); freq=math.floor(freq / 100)
                if freq<49 and freq>51: print(f"slvId:{slvId}, freq:{freq} ({rr[3]})")

        mb.client_get().close()

if __name__ == '__main__':
        
        gmbClient = mb.client_get()
        
        while(True):
                modbus_tcp_access_loop(host)