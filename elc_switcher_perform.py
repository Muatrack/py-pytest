
import   components.device.elc_platform  as ElcPt
from     components.protocol.http   import client
import time

""" 
    电力网关子设备分合闸操作
    通过平台下发指定空开的分合闸操作
"""

_httpClient = client.Client()
_platform   = ElcPt.Platform(_httpClient)

def turnSlaveOn(gwSn:str, slvSn:str):
    _platform.gatewaySelect("E10132E4952250A3")
    _platform.slaveSelect("150802DB9422015F")
    resp = _platform.slaveTrunOff()
    time.sleep(5)
    resp = _platform.slaveTrunOn()
    time.sleep(5)
    resp = _platform.slaveTrunOff()
    time.sleep(5)
    resp = _platform.slaveTrunOn()
    time.sleep(5)
    resp = _platform.slaveTrunOff()
    time.sleep(5)
    resp = _platform.slaveTrunOn()


if __name__ == '__main__':
    turnSlaveOn('', '')