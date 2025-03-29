import pytest
import requests
# import responses_validator
import time
from itower_http_api_lib import *

def http_api_1_5_sw_on(id:int):
    """
        合闸封装
    """
    http_api_1_5(id, Api5CtlCls.SW_ON)

def http_api_1_5_sw_off(id:int):
    """
        分闸封装
    """
    http_api_1_5(id, Api5CtlCls.SW_OFF)

def http_api_1_5_air_on(id:int):
    """
        空调机开机封装
    """
    http_api_1_5(id, Api5CtlCls.AIR_ON)

def http_api_1_5_air_off(id:int):
    """
        空调机关机封装
    """
    http_api_1_5(id, Api5CtlCls.AIR_OFF)

#------------------------------------------------------------------------------------------------------#

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

    # http_api_1_6(destSlaveId, {"name":"base64"}); time.sleep(2)     # 修改子设备名称
    # http_api_1_6(destSlaveId, {"pid":0}); time.sleep(2)             # 修改子设备父id

@pytest.mark.repeat(1)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_query():
    """
        查询设备
    """
    resp = http_api_1_1()
    assert resp.status_code==200
    assert resp.json()['code']==1000
    print( resp.text )
    time.sleep(1)

'''
@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_power_switch():
    """
        分合闸循环
        
        依赖 test_http_api_slave_query 查询结果
        遍历列表中属于采集器的类型设备，进行分合闸控制
    """
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


@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ac_switch():
    """
        空调开关机循环

        依赖 test_http_api_slave_query 查询结果
        遍历列表中属于采集器的类型设备，进行分合闸控制
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_add():
    """
        增加设备

        依赖 test_http_api_slave_query 查询结果
        记录、对比 操作前后的设备数量的变化判定操作的成功与否
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_del():
    """
        删除设备

        依赖 test_http_api_slave_add 增加的设备
        记录、对比 操作前后的设备数量的变化、操作前后设备id对比、判定操作是否成功
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_slave_mod():
    """
        修改设备

        执行查询设备列表，对指定id修改名称，再次查询设备列表读取指定id设备的名称，对比查询到的name与修改时写入的name是否相同
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ctler_fwver():
    """
        读取控制器的固件版本
    """
    pass

@pytest.mark.repeat(10)
@pytest.mark.http_api_itower_controller
def test_http_api_ctler_ota():
    """
        控制器升级
    """
    pass

'''