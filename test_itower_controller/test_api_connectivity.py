import pytest
import requests
# import responses_validator
import time
from itower_http_api_lib import *

def http_api_1_5_sw_on(id:int):
    http_api_1_5(id, Api5CtlCls.SW_ON)

def http_api_1_5_sw_off(id:int):
    http_api_1_5(id, Api5CtlCls.SW_OFF)

def http_api_1_5_air_on(id:int):
    http_api_1_5(id, Api5CtlCls.AIR_ON)

def http_api_1_5_air_off(id:int):
    http_api_1_5(id, Api5CtlCls.AIR_OFF)

# @pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_all():
    """
        全部HTTP API调用一次

        检查请求的连通性，仅检查http api的相应值
    """
    
    http_api_1_1(); time.sleep(2)                       # 查询设备列表
    http_api_1_2(); time.sleep(2)                       # 查询设备的采集数据
    # 增加设备，名称：自动添加设备， SN：170902FB23DDEEFF
    # http_api_1_3(name="6Ieq5Yqo5re75Yqg6K6+5aSH", sn="170902FB23DDEEFF"); time.sleep(2)

    durationTs = 3
    repeatCount = 10
    while( repeatCount>0 ):
        destSlaveId = 11        
        http_api_1_5_sw_off(destSlaveId); time.sleep(durationTs)     # 发起分闸
        http_api_1_5_sw_on(destSlaveId); time.sleep(durationTs)      # 发起合闸
        http_api_1_5_air_off(destSlaveId); time.sleep(durationTs)    # 发起开机
        http_api_1_5_air_on(destSlaveId); time.sleep(durationTs)     # 发起关机

        destSlaveId = 13
        http_api_1_5_sw_off(destSlaveId); time.sleep(durationTs)     # 发起分闸
        http_api_1_5_sw_on(destSlaveId); time.sleep(durationTs)      # 发起合闸
        http_api_1_5_air_off(destSlaveId); time.sleep(durationTs)    # 发起开机
        http_api_1_5_air_on(destSlaveId); time.sleep(durationTs)     # 发起关机

        destSlaveId = 18
        http_api_1_5_sw_off(destSlaveId); time.sleep(durationTs)     # 发起分闸
        http_api_1_5_sw_on(destSlaveId); time.sleep(durationTs)      # 发起合闸
        http_api_1_5_air_off(destSlaveId); time.sleep(durationTs)    # 发起开机
        http_api_1_5_air_on(destSlaveId); time.sleep(durationTs)     # 发起关机

        repeatCount-=1

    # http_api_1_6(destSlaveId, {"name":"base64"}); time.sleep(2)     # 修改子设备名称    
    # http_api_1_6(destSlaveId, {"pid":0}); time.sleep(2)             # 修改子设备父id