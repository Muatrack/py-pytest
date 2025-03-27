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
def test_http_api_1_1():
    http_api_1_1(); time.sleep(2)
    http_api_1_2(); time.sleep(2)

    # 子设备id
    destSlaveId = 1
    # 发起分闸
    http_api_1_5_sw_off(destSlaveId); time.sleep(5)
    # 发起合闸
    http_api_1_5_sw_on(destSlaveId); time.sleep(5)
    # 发起开机
    http_api_1_5_air_off(destSlaveId); time.sleep(5)
    # 发起关机
    http_api_1_5_air_on(destSlaveId); time.sleep(5)
    # 修改子设备名称
    http_api_1_6(destSlaveId, {"name":"base64"}); time.sleep(2)
    # 修改子设备父id
    http_api_1_6(destSlaveId, {"pid":0}); time.sleep(2)