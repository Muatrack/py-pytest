
import time
from ..protocol.http import interface

""" 
    封装平台使用的api
"""

class _SwEnum:
    SW_OFF  = 0
    SW_ON   = 1

class Platform:

    def __init__(self, httpClient:interface.ClientIF, host:str='http://backend.jiadiansystem.com', port:int=6011):
        self.httpClient = httpClient
        self.host_port = host+':'+str(port)

    def gatewaySelect(self, gwSn:str):
        '''
            设置控制目标的网关SN
        '''
        self.gwSn = gwSn

    def slaveSelect(self, slvSn:str):
        '''
            选择被控目标(断路器)的SN
        '''
        self.slvSn = slvSn

    def _makeSwitchUrl(self, swCtl:_SwEnum, path:str='/device-service/deviceBack/statusUpdate') -> str:      
        nowTm = int(time.time())
        url = f'{self.host_port}{path}?masterSn={self.gwSn}&status={swCtl}&subsetSn={self.slvSn}&_t={nowTm}'
        return url

    def slaveTrunOn(self):
        ''' 
            开启子设备开关 
            url: http://backend.jiadiansystem.com:6011/device-service/deviceBack/statusUpdate?masterSn=E10132E4952250A3&status=0&subsetSn=150802DB9422015F&_t=1748933447
        '''
        url:str = self._makeSwitchUrl(swCtl=_SwEnum.SW_ON)
        return self.httpClient.Get(url)

    def slaveTrunOff(self):
        ''' 
            关闭子设备开关 
            url: http://backend.jiadiansystem.com:6011/device-service/deviceBack/statusUpdate?masterSn=E10132E4952250A3&status=0&subsetSn=150802DB9422015F&_t=1748933447
        '''
        url:str = self._makeSwitchUrl(swCtl=_SwEnum.SW_OFF)
        return self.httpClient.Get(url)